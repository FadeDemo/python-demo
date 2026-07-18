import pandas as pd

df_users = pd.DataFrame(
    {"user_id": [1, 2, 3], "membership": ["Gold", "Silver", "Bronze"]}
)
mapping_dict = {"Bronze": 1, "Silver": 2, "Gold": 3}
# 使用 .map() 将字典应用到列上
df_users["membership_encoded"] = df_users["membership"].map(mapping_dict)
print(df_users)
