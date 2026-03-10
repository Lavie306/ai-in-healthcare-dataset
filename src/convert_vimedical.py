import os
import json
import re
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util

# Cấu hình thiết bị: Ưu tiên GPU nếu có
device = "cuda" if torch.cuda.is_available() else "cpu"

corpus_dir = "../data_raw/ViMedical/Corpus_Redone"
question_dir = "../data_raw/ViMedical/Question_for_dataset"
output_csv = "../data_clean/medical_dataset.csv"
output_json = "../data_clean/medical_dataset.json"

# Load model một lần và chuyển sang device
model = SentenceTransformer("keepitreal/vietnamese-sbert", device=device)


def split_paragraphs(text):
    paragraphs = re.split(r"\n|\d+\.|;", text)
    return [p.strip() for p in paragraphs if len(p) > 40]


data = []
files = [f for f in os.listdir(question_dir) if f.endswith(".txt")]

print(f"Bắt đầu xử lý {len(files)} files trên {device}...")

for q_file in files:
    corpus_path = os.path.join(corpus_dir, q_file)
    question_path = os.path.join(question_dir, q_file)

    if not os.path.exists(corpus_path):
        continue

    # Đọc dữ liệu
    with open(question_path, "r", encoding="utf8") as f:
        questions = [q.strip() for q in f.readlines() if q.strip()]
    with open(corpus_path, "r", encoding="utf8") as f:
        paragraphs = split_paragraphs(f.read())

    if not paragraphs or not questions:
        continue

    # --- TỐI ƯU HÓA TẠI ĐÂY ---
    # 1. Encode toàn bộ paragraphs của file này MỘT LẦN DUY NHẤT
    p_embeddings = model.encode(paragraphs, convert_to_tensor=True, batch_size=32)

    # 2. Encode toàn bộ questions của file này MỘT LẦN DUY NHẤT
    q_embeddings = model.encode(questions, convert_to_tensor=True, batch_size=32)

    # 3. Tính toán ma trận tương đồng (Cosine Similarity Matrix)
    # Kết quả là ma trận kích thước (số câu hỏi x số đoạn văn)
    cos_scores = util.cos_sim(q_embeddings, p_embeddings)

    for i, q in enumerate(questions):
        q_lower = q.lower()

        # Logic lọc theo từ khóa (vẫn giữ nguyên logic của bạn nhưng áp dụng nhanh hơn)
        keywords = []
        if "triệu chứng" in q_lower or "bệnh gì" in q_lower:
            keywords = ["triệu chứng", "dấu hiệu"]
        elif "nguyên nhân" in q_lower:
            keywords = ["nguyên nhân"]
        elif "điều trị" in q_lower:
            keywords = ["điều trị", "chữa"]
        elif "phòng ngừa" in q_lower:
            keywords = ["phòng", "ngừa"]

        # Tìm index có score cao nhất
        if keywords:
            # Chỉ lấy các index của paragraph chứa từ khóa
            valid_indices = [idx for idx, p in enumerate(paragraphs)
                             if any(k in p.lower() for k in keywords)]

            if valid_indices:
                # Lọc scores của những paragraph thỏa mãn từ khóa
                sub_scores = cos_scores[i][valid_indices]
                best_idx = valid_indices[sub_scores.argmax().item()]
            else:
                best_idx = cos_scores[i].argmax().item()
        else:
            best_idx = cos_scores[i].argmax().item()

        data.append({
            "question": q,
            "answer": paragraphs[best_idx]
        })

# Lưu kết quả
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False, encoding="utf-8-sig")
with open(output_json, "w", encoding="utf8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Hoàn thành! Tổng số QA: {len(df)}")