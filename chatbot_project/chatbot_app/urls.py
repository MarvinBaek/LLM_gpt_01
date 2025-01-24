from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),  # 기본 URL을 chat 뷰로 연결
    path('response/', views.response, name='response'),  # 챗봇 답변 페이지
]
