import pandas as pd

# 用户特征表
df_users = pd.DataFrame({
    'user_id': [1, 2, 3, 4],
    'age': [25, 32, 45, 22],
    'city': ['NY', 'SF', 'LA', 'NY']
})

# 交易行为表
df_transactions = pd.DataFrame({
    'user_id': [1, 2, 4, 5],
    'total_spent': [250.5, 890.0, 120.0, 50.0],
    'purchase_count': [3, 10, 1, 1]
})

# 按照 'user_id' 将交易数据合并到用户表
df_train = pd.merge(df_users, df_transactions, on='user_id', how='left')
print(df_train)

# 填充缺失值为 0
df_train['total_spent'] = df_train['total_spent'].fillna(0)
df_train['purchase_count'] = df_train['purchase_count'].fillna(0)

print(df_train)
