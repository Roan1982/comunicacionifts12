from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('topics/', views.topics, name='topics'),
    path('quiz/<int:quiz_id>/', views.quiz, name='quiz'),
    path('quiz/<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
    path('toggle_progress/<int:topic_id>/', views.toggle_progress, name='toggle_progress'),
]