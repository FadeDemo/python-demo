import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 模拟数据
df = pd.DataFrame(
    {"age": [25, 32, 45, 22, 60], "income": [45000, 60000, 120000, 35000, 80000]}
)

# 初始化归一化器
min_max_scaler = MinMaxScaler()

# 拟合并转换数据
df_minmax = pd.DataFrame(min_max_scaler.fit_transform(df), columns=df.columns)
print(df_minmax)
