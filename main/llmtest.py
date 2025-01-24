from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv('D:\AI\LLM\.env')

#API Key 설정
client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))


#모델 설정
chat_completion = client.chat.completions.create(
  messages =[
    {"role": "system", "content": "You are a tour guide in 나트랑"},
    {"role": "user", "content": "나트랑은 어떤 곳이야"}
  ],
  model = "o1-2024-12-17"
)

# 생성된 응답 출력
print(chat_completion.choices[0].message.content)
