import numpy as np


def cosine_similarity(v1, v2):
    # 1. 计算点积 (分子)
    dot_product = np.dot(v1, v2)

    # 2. 计算向量的长度 (分母)
    # np.linalg.norm 用于计算向量的欧几里得长度 (L2 范数)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    # 3. 计算余弦相似度
    # 添加一个小常数 1e-9 防止除以 0 的错误
    similarity = dot_product / (norm_v1 * norm_v2 + 1e-9)
    return similarity


# 模拟：假设这是“苹果”和“橘子”的文本向量 (在多维空间中比较接近)
fruit1 = np.array([0.8, 0.1, 0.2])
fruit2 = np.array([0.7, 0.2, 0.1])

# 模拟：假设这是“汽车”的文本向量 (与水果差异很大)
car = np.array([0.1, 0.9, 0.8])

print(f"苹果与橘子的相似度: {cosine_similarity(fruit1, fruit2):.4f}")  # 结果接近 1
print(f"苹果与汽车的相似度: {cosine_similarity(fruit1, car):.4f}")  # 结果远小于 1
