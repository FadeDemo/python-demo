text = "AI is great and AI is the future"
words = text.split()  # 将文本按空格分割成单词列表
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
# 输出: {'AI': 2, 'is': 2, 'great': 1, 'and': 1, 'the': 1, 'future': 1}
print(word_counts)
words = ["AI", "Machine", "Learning", "RAG"]
word_lengths = {word: len(word) for word in words}
# 输出: {'AI': 2, 'Machine': 7, 'Learning': 8, 'RAG': 3}
print(word_lengths)
prices_usd = {"book": 15, "keyboard": 80, "mouse": 25, "monitor": 300}

# 只保留价格大于 50 的，并乘以 7.2 转换为 CNY
prices_cny = {item: price * 7.2 for item,
              price in prices_usd.items() if price > 50}

# 输出: {'keyboard': 576.0, 'monitor': 2160.0}
print(prices_cny)
user_ids = [101, 102, 103]
user_names = ["Alice", "Bob", "Charlie"]

user_dict = {user_id: name for user_id, name in zip(user_ids, user_names)}
# 输出: {101: 'Alice', 102: 'Bob', 103: 'Charlie'}
