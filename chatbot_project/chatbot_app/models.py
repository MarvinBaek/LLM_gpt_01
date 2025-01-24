from django.db import models

class Conversation(models.Model):
    user_input = models.TextField()  # 사용자가 입력한 내용
    chatbot_reply = models.TextField()  # 챗봇의 답변
    created_at = models.DateTimeField(auto_now_add=True)  # 대화한 시간

    def __str__(self):
        return f"User: {self.user_input} / Chatbot: {self.chatbot_reply}"
