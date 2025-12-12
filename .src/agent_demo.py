import os
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

# 使用 DeepSeek API（OpenAI 兼容）
# API key 从环境变量 DEEPSEEK_API_KEY 读取
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    # 如果当前会话没有环境变量，尝试从用户级别环境变量读取
    import sys
    if sys.platform == "win32":
        import subprocess
        try:
            result = subprocess.run(
                ['powershell', '-Command', '[System.Environment]::GetEnvironmentVariable("DEEPSEEK_API_KEY", "User")'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0 and result.stdout.strip():
                api_key = result.stdout.strip()
        except:
            pass
    
    if not api_key:
        raise ValueError(
            "未找到 DEEPSEEK_API_KEY 环境变量。\n"
            "请执行以下操作之一：\n"
            "1. 在当前终端运行: $env:DEEPSEEK_API_KEY=\"你的key\"\n"
            "2. 或者重新打开终端（如果已通过 setx 设置）"
        )

model = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=api_key,
)

agent = create_agent(
    model=model,
    tools=[multiply],
    system_prompt="You are a helpful assistant that can perform calculations.",
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is 13 times 7?"}]}
)

print(result)
