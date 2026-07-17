import pandas as pd

# 模拟数据
data = {'doc_id': [1, 2, 3, 4],
        'content': ['RAG 介绍', None, '向量数据库', '提示词工程'],
        'word_count': [500, 0, 800, 120]}
df = pd.DataFrame(data)
# 丢弃缺失值
df_cleaned = df.dropna(subset=['content'])
# 筛选
high_quality_docs = df_cleaned[df_cleaned['word_count'] > 200]
print(high_quality_docs)
