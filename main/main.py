import openai
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# API Key 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# 프롬프트 명령
prompt = "너는 오늘 배운 것들을 정리하는 친절한 TIL 챗봇이야. 사용자가 오늘 하루 동안 배운 점이나 중요한 경험을 돌아볼 수 있도록 돕고, 그들이 배운 것을 잘 정리할 수 있게 도와줘."


messages = [{"role": "system", "content": prompt}]

# exit가 입력되기 전까지 계속 대화
with open("chat_log.txt", "w", encoding="utf-8") as file:
    while True:
        # 사용자 입력 받기
        user_input = input("사용자: ")

        if user_input.lower() == "exit":
            print("종료합니다.")
            break

        # 사용자 입력 값을 대화 목록에 추가 (대화의 흐름을 기억시키기 위해)
        messages.append({"role": "user", "content": user_input})

        # GPT4o로 설정
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages
        )

        #GPT야 대답
        assistant_reply = response['choices'][0]['message']['content']

        # 대답 출력
        print(f"GPT: {assistant_reply}\n")

        #GPT 출력 값을 대화 목록에 추가(대화의 흐름을 기억시키기 위해)
        messages.append({"role": "assistant", "content": assistant_reply})

        # 대화 내용 기록
        file.write(f"사용자: {user_input}\n")
        file.write(f"GPT: {assistant_reply}\n\n")