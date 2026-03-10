import pandas as pd
import re


def clean_text(text):
    text = str(text).lower()
    text = text.strip()

    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\sàáảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ]', '', text)
    return text


def clean_dataframe(df):

    # remove null
    df = df.dropna()

    # remove duplicate
    df = df.drop_duplicates()

    # clean text
    df["question"] = df["question"].apply(clean_text)
    df["answer"] = df["answer"].apply(clean_text)

    return df