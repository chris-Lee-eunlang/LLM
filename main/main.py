from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv('D:\AI\LLM\.env')

#API Key 설정
client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))


#모델 설정

while True:
  user_input = input("질문을 입력하세요: ")
  if user_input == "exit":
    break
  chat_completion = client.chat.completions.create(
    messages =[
      {"role": "system", "content": "You are a tour guide in 나트랑"},
      {"role": "user", "content": user_input}
    ],
    model = "gpt-4o-mini"
  )
  print(chat_completion.choices[0].message.content)
  file_path = "chat.txt"
  with open(file_path, "a", encoding="utf-8") as file:  # "a" 모드를 사용하여 파일에 추가
    file.write(str(chat_completion.choices[0].message.content) + "\n")