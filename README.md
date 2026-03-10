
# Vietnamese Medical QA Dataset – Data Processing

## 1. Giới thiệu

Project này tập trung vào việc **thu thập, xử lý và chuẩn hóa dữ liệu câu hỏi – trả lời (Question Answering)** trong lĩnh vực y tế tiếng Việt.

Mục tiêu của project là tạo ra **một dataset QA y tế sạch và có cấu trúc chuẩn**, phục vụ cho:

* Huấn luyện mô hình NLP
* Xây dựng chatbot y tế
* Nghiên cứu Question Answering

Dataset được tổng hợp từ nhiều nguồn dữ liệu y tế tiếng Việt khác nhau.

---

# 2. Cấu trúc thư mục

```id="structure_tree"
project/
│
├── .venv/                 # Cài đặt thư viện  
│
├── data_raw/              # Dữ liệu gốc
│   ├── mental_health_vi
│   ├── vi-HealthQA
│   ├── ViHealthQA
│   ├── ViHealthQA-small
│   └── ViMedical
│
├── data_clean/            # Dataset sau khi chuyển đổi định dạng
│   ├── medical_dataset.csv
│   ├── medical_dataset.json
│   ├── medical_data_combined.csv
│   ├── medical_data_combined.json
│   ├── ViHealthQA_combined.csv
│   └── ViHealthQA_combined.json
│
├── data_processed/        # Dataset sau khi xử lý hoàn chỉnh
│   ├── final_medical_qa_dataset.csv
│   ├── final_medical_qa_dataset.json
│   ├── train.csv
│   ├── val.csv
│   └── test.csv
│
├── notebooks/             # Notebook xử lý và phân tích dữ liệu
│   ├── merge_data.ipynb
│   ├── explore_data_csv.ipynb
│   ├── explore_data_parquet.ipynb
│   └── data_split.ipynb
│
├── src/                   # Source code xử lý dữ liệu
│   ├── convert_vimedical.py
│   ├── load_data.py
│   ├── merge_datasets.py
│   └── preprocessing.py
│
├── requirements.txt
└── README.md
```

---

# 3. Quy trình xử lý dữ liệu

Pipeline xử lý dataset gồm các bước sau:

### Bước 1: Thu thập dữ liệu

Dữ liệu được lấy từ nhiều nguồn QA y tế:

* ViMedical
* ViHealthQA
* mental_health_vi

Các dữ liệu này được lưu trong thư mục:

```
data_raw/
```

---

### Bước 2: Chuyển đổi định dạng

Dữ liệu từ các nguồn khác nhau được **chuyển đổi về định dạng chung**:

```
question
answer
```

Sau bước này dữ liệu được lưu vào:

```
data_clean/
```

---

### Bước 3: Gộp dataset

Các dataset sau khi chuẩn hóa được **gộp lại thành một dataset lớn**.

Notebook thực hiện:

```
notebooks/merge_data.ipynb
```

Kết quả:

```
final_medical_qa_dataset.csv
```

---

### Bước 4: Làm sạch dữ liệu

Các bước làm sạch gồm:

* loại bỏ dòng dữ liệu bị thiếu
* loại bỏ cặp QA trùng hoàn toàn
* kiểm tra chất lượng dữ liệu

Script xử lý:

```
src/preprocessing.py
```

---

### Bước 5: Chia tập train / validation / test

Dataset cuối được chia thành:

* **Train:** 80%
* **Validation:** 10%
* **Test:** 10%

Notebook thực hiện:

```
notebooks/data_split.ipynb
```

Kết quả lưu tại:

```
data_processed/
```

---

# 4. Định dạng dữ liệu

Dataset QA có cấu trúc như sau:

| question                              | answer                                      |
| ------------------------------------- | ------------------------------------------- | 
| Triệu chứng của bệnh Alzheimer là gì? | Các triệu chứng bao gồm suy giảm trí nhớ... |

---

# 5. Cài đặt môi trường

Cài đặt các thư viện cần thiết:

```
pip install -r requirements.txt
```

Các thư viện chính:

* pandas
* numpy
* scikit-learn
* jupyter

---

# 6. Cách chạy project

### Bước 1 – Khám phá dữ liệu

```
notebooks/explore_data_csv.ipynb
```

### Bước 2 – Gộp dataset

```
notebooks/merge_data.ipynb
```

### Bước 3 – Chia train / val / test

```
notebooks/data_split.ipynb
```

---

# 7. Dataset cuối cùng

Sau khi xử lý, dataset cuối nằm trong:

```
data_processed/
```

Bao gồm:

* `train.csv`
* `val.csv`
* `test.csv`

Dataset này có thể dùng để:

* huấn luyện mô hình QA
* xây dựng chatbot y tế
* nghiên cứu NLP tiếng Việt

---

# 8. Tác giả

Project xử lý dữ liệu cho **Vietnamese Medical QA Dataset**.
=======
# ai-in-healthcare-dataset
Vietnamese medical question answering dataset for AI in healthcare.
>>>>>>> a9086e9679fa5ad55bb80b1d1fb09a1aa70a9f15
