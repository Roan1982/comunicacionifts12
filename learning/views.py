from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Topic, Quiz, Question, UserProgress
import json

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'learning/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'learning/home.html')

@login_required
def topics(request):
    topics = Topic.objects.all().order_by('order')
    completed_topics = set(p.topic.id for p in UserProgress.objects.filter(user=request.user, completed=True))
    total_topics = topics.count()
    completed_count = len(completed_topics)
    progress_percentage = (completed_count / total_topics * 100) if total_topics > 0 else 0
    return render(request, 'learning/topics.html', {'topics': topics, 'completed_topics': completed_topics, 'progress_percentage': progress_percentage})

@login_required
def quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()
    return render(request, 'learning/quiz.html', {'quiz': quiz, 'questions': questions})

@login_required
def submit_quiz(request, quiz_id):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = quiz.question_set.all()
        score = 0
        total = questions.count()
        results = []
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            correct = user_answer and int(user_answer) == question.correct_answer
            if correct:
                score += 1
            results.append({
                'question': question.question_text,
                'user_answer_text': question.option1 if user_answer == '1' else question.option2 if user_answer == '2' else question.option3 if user_answer == '3' else 'No respondida',
                'correct_answer_text': question.option1 if question.correct_answer == 1 else question.option2 if question.correct_answer == 2 else question.option3,
                'is_correct': correct
            })
        percentage = (score / total * 100) if total > 0 else 0
        
        # Mark topic as completed if quiz passed (e.g., 70% or more)
        if quiz.topic and percentage >= 70:
            UserProgress.objects.update_or_create(
                user=request.user,
                topic=quiz.topic,
                defaults={'completed': True}
            )
        
        if score == total:
            message = "¡Excelente! Has acertado todas las preguntas."
            message_class = "text-success"
        elif score >= total / 2:
            message = "Buen trabajo. Revisa los temas que no entendiste."
            message_class = "text-warning"
        else:
            message = "Necesitas estudiar más. Revisa todos los temas."
            message_class = "text-danger"
        return render(request, 'learning/results.html', {
            'score': score, 
            'total': total, 
            'percentage': percentage, 
            'message': message, 
            'message_class': message_class, 
            'quiz_id': quiz_id,
            'results': results
        })
    return redirect('quiz', quiz_id=quiz_id)

@login_required
def toggle_progress(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    progress, created = UserProgress.objects.get_or_create(user=request.user, topic=topic)
    progress.completed = not progress.completed
    progress.save()
    return JsonResponse({'completed': progress.completed})
