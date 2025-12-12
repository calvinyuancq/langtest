import os
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# 创建模型实例，使用 DeepSeek API（OpenAI 兼容）
# API key 从环境变量 DEEPSEEK_API_KEY 读取
model = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # 从环境变量读取
)

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

print(result)

