import numpy as np

# 1. 创建向量 (一维数组)
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# 2. 逐元素运算 (Element-wise)
# 对应位置的元素相加或相乘
add_result = vector_a + vector_b      # 输出: [5, 7, 9]
mul_result = vector_a * vector_b      # 输出: [4, 10, 18] -> 注意：这不是矩阵乘法！

# 3. 点积 (Dot Product) / 矩阵乘法
# 向量的点积是将对应元素相乘后再求和：1*4 + 2*5 + 3*6 = 32
dot_result = np.dot(vector_a, vector_b)
# 或者使用 Python 3.5+ 引入的 @ 运算符，这在 AI 代码中极其常见
dot_result_alt = vector_a @ vector_b    # 输出: 32

# 4. 矩阵与向量相乘 (常用于批量处理)
matrix = np.array([[1, 2], [3, 4], [5, 6]])  # 3行2列的矩阵
print(matrix.shape)  # 输出: (3, 2)
vector = np.array([10, 20])                 # 长度为2的向量
print(vector.shape)  # 输出: (2,)
result = matrix @ vector                    # 输出: [50, 110, 170]
print(result)
vector_2d = np.array([[10],
                      [20]])
result_2d = matrix @ vector_2d              # 结果形状: (3, 1)
print(result_2d)
