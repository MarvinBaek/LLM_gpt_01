import openai
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# API Key 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# 프롬프트 명령
prompt = "넌 최고의 학생이야."

messages = [{"role": "system", "content": prompt}]

# exit가 입력되기 전까지 계속 대화
while True:
    # 사용자 입력 받기
    user_input = input("사용자: ")

    if user_input.lower() == "그만":
        print("종료합니다.")
        break

    # 사용자 입력 값을 대화 모곩에 추가 (대화의 흐름을 기억시키기 위해)
    messages.append({"role": "user", "content": user_input})

    # GPT3.5로 설정
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    #GPT야 대답
    assistant_reply = response['choices'][0]['message']['content']

    # 대답 출력
    print(f"GPT: {assistant_reply}\n")

    #GPT 출력 값을 대화 목록에 추가(대화의 흐름을 기억시키기 위해)
    messages.append({"role": "assistant", "content": assistant_reply})