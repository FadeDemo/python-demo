# 定义一个父类（基类）
class BaseLLM:
    def __init__(self, model_name, api_key):
        self.model_name = model_name
        self.api_key = api_key

    def count_tokens(self, text):
        # 假设这是一个通用的基础 token 统计方法
        print(f"[{self.model_name}] 正在计算 '{text}' 的 Token 数量...")
        return len(text)


# 定义一个子类，继承自 BaseLLM


class OpenAILLM(BaseLLM):
    def __init__(self, model_name, api_key, organization_id):
        # 使用 super() 调用父类的初始化方法
        super().__init__(model_name, api_key)
        self.organization_id = organization_id

    def generate_response(self, prompt):
        print(f"使用 OpenAI API 发送请求: {prompt}")
        return "这是来自 ChatGPT 的回复"


# 实例化子类
my_gpt = OpenAILLM(model_name="gpt-4", api_key="sk-xxx", organization_id="org-123")

# 子类可以直接使用父类的方法
token_count = my_gpt.count_tokens("你好，世界")

# 子类也有自己独有的方法
response = my_gpt.generate_response("什么是 RAG？")

# 另一个子类，同样继承自 BaseLLM (假设前面的代码已经运行)


class LocalLLM(BaseLLM):
    def __init__(self, model_name, model_path):
        # 本地模型不需要 api_key，我们传 None
        super().__init__(model_name, api_key=None)
        self.model_path = model_path

    # 注意：这里的方法名和 OpenAILLM 中的一致
    def generate_response(self, prompt):
        print(f"从本地路径 {self.model_path} 加载模型并推理...")
        return "这是来自本地 LLaMA 模型的回复"


# 【多态的核心体现】：一个接收任何模型的通用函数


def run_ai_task(model, prompt):
    print("--- 任务开始 ---")
    # 不管传入的是 OpenAILLM 还是 LocalLLM，
    # 只要它们都有 generate_response 方法，就能正常运行。
    result = model.generate_response(prompt)
    print(f"最终结果: {result}")
    print("--- 任务结束 ---\n")


# 测试多态
gpt_model = OpenAILLM("gpt-3.5", "sk-xxx", "org-123")
llama_model = LocalLLM("llama-2-7b", "/models/llama2")

# 同一个函数，传入不同的对象，表现出不同的行为
run_ai_task(gpt_model, "请写一首诗。")
run_ai_task(llama_model, "请写一首诗。")
