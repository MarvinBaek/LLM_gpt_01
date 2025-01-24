from django.http import JsonResponse
from django.shortcuts import render
from .chatbot_logic import get_chatbot_response

# 대화 입력 화면
def chat(request):
    conversation = request.session.get('conversation', [])
    return render(request, 'chatbot_app/chat.html', {'conversation': conversation})

# 챗봇 응답 페이지 (AJAX 요청 처리)
def response(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input')

        # 사용자가 '초기화'를 입력한 경우 대화 기록 초기화
        if user_input.lower() == "초기화":
            request.session['conversation'] = []  # 세션에서 대화 기록 초기화
            return JsonResponse({
                'user_input': user_input,
                'chatbot_reply': '대화가 초기화되었습니다.',
                'conversation': []  # 빈 대화 내용 반환
            })

        # 세션에 대화 내용 저장 (세션이 없으면 새로 시작)
        conversation = request.session.get('conversation', [])

        # 챗봇 응답을 생성
        chatbot_reply = get_chatbot_response(user_input)

        # 세션에 대화 내용 추가
        conversation.append({'role': 'user', 'content': user_input})
        conversation.append({'role': 'assistant', 'content': chatbot_reply})

        # 세션에 대화 내용 저장
        request.session['conversation'] = conversation

        # JSON 형식으로 응답 반환 (AJAX 처리를 위한 데이터)
        return JsonResponse({
            'user_input': user_input,
            'chatbot_reply': chatbot_reply,
            'conversation': conversation  # 전체 대화 내용 전달
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)
