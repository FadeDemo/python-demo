import pandas as pd
data = [
    {"id": 1, "text": "Python 是一种强大的语言。", "category": "tech"},
    {"id": 2, "text": "今天天气很好。", "category": "daily"},
    {"id": 3, "text": "NumPy 用于科学计算。", "category": "tech"}
]
df = pd.DataFrame(data)
print(df)
tech_docs = df[df['category'] == 'tech']
print(tech_docs['text'].tolist())
