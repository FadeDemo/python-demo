import pandas as pd

# 我们的训练集，包含了城市数据
df_train = pd.DataFrame(
    {"user_id": [1, 2, 3, 4], "age": [25, 32, 45, 22], "city": ["NY", "SF", "LA", "NY"]}
)
# 对 'city' 列进行 One-Hot 编码
df_encoded = pd.get_dummies(df_train, columns=["city"])

# Pandas 会自动识别出文本列（如果你不指定 columns），但显式指定通常更安全。
print(df_encoded)
df_encoded = pd.get_dummies(df_train, columns=["city"], dtype=int)
print(df_encoded)
