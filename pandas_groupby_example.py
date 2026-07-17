import pandas as pd

# 包含文档来源、分类、字数和人工质量评分的 RAG 知识库数据
data = {
    'source': ['wiki', 'wiki', 'blog', 'blog', 'news', 'news', 'news'],
    'category': ['science', 'history', 'tech', 'tech', 'politics', 'tech', 'politics'],
    'word_count': [1200, 800, 3000, 2500, 400, 600, 550],
    'quality_score': [0.9, 0.85, 0.95, 0.7, 0.6, 0.8, 0.65]
}
df = pd.DataFrame(data)
# 按 category 拆分，并统计每个类别的数量
category_distribution = df.groupby('category').size()
print(category_distribution)

# 结果显示 tech 类有 3 篇，而 science 只有 1 篇，这提示我们需要补充 science 类别的数据。
# 评估不同数据源的平均字数和平均质量
source_stats = df.groupby('source').agg({
    'word_count': 'mean',
    'quality_score': 'mean'
})
print(source_stats)

# 结果可能显示 blog 的平均字数远超 news，这意味我们需要对 blog 使用更大的 Chunk Size。
# 自定义函数：计算每个分类中最长文档和最短文档的字数差值，评估长度波动


def range_diff(series):
    return series.max() - series.min()


# 应用自定义聚合函数
word_count_range = df.groupby('category')['word_count'].agg(range_diff)
print(word_count_range)
