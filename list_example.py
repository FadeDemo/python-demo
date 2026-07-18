scores = [45, 78, 92, 55, 88, 60]
passed_scores = []
for score in scores:
    if score >= 60:
        passed_scores.append(score)
print(passed_scores)
# 列表推导式
prices = [100, 50, 80, 200]
new_prices = [price * 1.1 for price in prices]
# 输出: [110.0, 55.0, 88.0, 220.0]
print(new_prices)
temperatures = [22, -999, 24, 25, -999, 21]
valid_temps = [temp for temp in temperatures if temp > -50]
# 输出: [22, 24, 25, 21]
print(valid_temps)
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [n**2 for n in numbers if n % 2 == 0]
# 输出: [4, 16, 36]
print(even_squares)
raw_words = ["  Apple ", "banana", " CHERRY\n"]
clean_words = [word.strip().lower() for word in raw_words]
# 输出: ['apple', 'banana', 'cherry']
print(clean_words)
users = [
    {"name": "Alice", "age": 28, "role": "admin"},
    {"name": "Bob", "age": 22, "role": "user"},
    {"name": "Charlie", "age": 35, "role": "admin"},
]

# 提取所有管理员的名字
admin_names = [user["name"] for user in users if user["role"] == "admin"]
# 输出: ['Alice', 'Charlie']
print(admin_names)
