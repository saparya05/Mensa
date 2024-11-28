from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomSignupForm, CustomLoginForm
from .models import DiaryEntry
import speech_recognition as sr
from gtts import gTTS
from transformers import pipeline
from django.http import JsonResponse
from django.shortcuts import render
import os
from io import BytesIO


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup_view(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomSignupForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = CustomLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def activities(request):
    return render(request, 'activities.html')


@login_required
def diary(request):
    if request.method == 'POST':
        entry_id = request.POST.get('entry_id')
        action = request.POST.get('action')

        if action == 'edit' and entry_id:
            entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
            title = request.POST.get('title')
            content = request.POST.get('content')
            if content:
                entry.title = title
                entry.content = content
                entry.save()
                print("Entry updated successfully!")
            else:
                print("Content cannot be empty.")

        elif action == 'delete' and entry_id:
            entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
            entry.delete()
            print("Entry deleted successfully!")

        return redirect('diary')

    entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'diary.html', {'entries': entries})

@login_required
def mood(request):
    return render(request, 'mood.html')



# chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')

def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        
        if user_message:
            # Generate response from the chatbot
            response = chatbot(user_message)
            bot_reply = response[0]['generated_text']
            
            # Convert bot reply to speech
            tts = gTTS(text=bot_reply, lang='en')
            speech_fp = BytesIO()
            tts.save(speech_fp)
            speech_fp.seek(0)
            
            # Return bot's response in text and speech
            return JsonResponse({
                'text': bot_reply,
                'speech': speech_fp.getvalue().decode('ISO-8859-1')  # Convert to a string format suitable for transfer
            })
        else:
            return JsonResponse({'error': 'No message provided'}, status=400)
    
    return render(request, 'chat/chatbot.html')

def speech_to_text(request):
    recognizer = sr.Recognizer()

    # Record audio from the user's microphone
    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)

    try:
        # Recognize the speech and convert to text
        user_input = recognizer.recognize_google(audio)
        print("You said: " + user_input)

        return JsonResponse({'text': user_input})
    except sr.UnknownValueError:
        return JsonResponse({'error': 'Sorry, I could not understand the audio.'}, status=400)
    except sr.RequestError:
        return JsonResponse({'error': 'Could not request results from Google Speech Recognition service.'}, status=500)
