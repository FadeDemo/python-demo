import pandas as pd
from sklearn.preprocessing import StandardScaler

# 模拟数据
df = pd.DataFrame(
    {"age": [25, 32, 45, 22, 60], "income": [45000, 60000, 120000, 35000, 80000]}
)

# 初始化标准化器
scaler = StandardScaler()

# 拟合并转换数据
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print(df_scaled)
