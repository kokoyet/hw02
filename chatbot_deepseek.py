"""
DeepSeek Chatbot 示例
运行环境：Python 3.8+
依赖安装：pip install openai python-dotenv
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 初始化DeepSeek客户端（兼容OpenAI格式）
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # 从环境变量读取
    base_url="https://api.deepseek.com"     # DeepSeek官方API地址
)

def chat_with_deepseek(user_input):
    """单轮对话函数"""
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  # 模型名称
            messages=[
                {"role": "system", "content": "你是一个有用的AI助手。"},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"调用出错：{str(e)}"

def main():
    print("=" * 50)
    print("DeepSeek Chatbot 已启动 (输入 'exit' 退出)")
    print("=" * 50)
    
    while True:
        user_input = input("\n👤 你: ")
        if user_input.lower() in ['exit', 'quit', '退出']:
            print("👋 再见！")
            break
        
        reply = chat_with_deepseek(user_input)
        print(f"\n🤖 助手: {reply}")

if __name__ == "__main__":
    main()