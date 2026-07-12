import numpy as np
from sentence_transformers import SentenceTransformer

# 1. 初始化本地 Embedding 模型（自动加载开源中文轻量模型）
print("正在加载语义嵌入模型...")
model = SentenceTransformer('shibing624/text2vec-base-chinese')

# 2. 准备测试文本
# 包含两篇计算机网络安全相关的核心摘要片段，以及一个无关的日常文本
documents = [
    "基于信任评估模型的车载自组织网络异常节点检测方案",  # 文档 0
    "智能网联汽车中针对协同合谋攻击的防御与缓解机制",    # 文档 1
    "今天的天气非常晴朗，空气质量很好，适合出门运动"     # 文档 2
]

# 3. 将文本转化为高维向量 (Embedding)
print("正在将文本转化为向量...")
embeddings = model.encode(documents)

# 打印向量的形状，看看文本变成了什么样
for i, emb in enumerate(embeddings):
    print(f"文档 {i} 的向量形状: {emb.shape}")  # 通常是 (768,) 维的向量

print("\n" + "="*40 + "\n")

# 4. 模拟用户提问 (Query)
query = "如何检测车载网络中的恶意节点和攻击行为？"
print(f"用户提问: '{query}'")
query_embedding = model.encode([query])[0]

# 5. 计算用户提问与各个文档的余弦相似度


def calculate_cosine(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-9)


print("\n--- 语义检索结果 ---")
for i, doc in enumerate(documents):
    similarity = calculate_cosine(query_embedding, embeddings[i])
    print(f"与 [文档 {i}] 的相似度: {similarity:.4f} -> 内容: {doc}")
