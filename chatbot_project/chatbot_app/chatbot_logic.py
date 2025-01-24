import openai
from django.conf import settings

# OpenAI API Key 설정
openai.api_key = settings.OPENAI_API_KEY

def get_chatbot_response(user_input):
    prompt = "너는 오늘 배운 것들을 정리하는 친절한 TIL 챗봇이야. 사용자가 오늘 하루 동안 배운 점이나 중요한 경험을 돌아볼 수 있도록 돕고, 그들이 배운 것을 잘 정리할 수 있게 도와줘."
    
    messages = [{"role": "system", "content": prompt}]
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # 또는 사용할 GPT 모델
        messages=messages
    )

    return response['choices'][0]['message']['content']
