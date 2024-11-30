from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomSignupForm, CustomLoginForm
from .models import DiaryEntry ,HealthMetric, Appointment, Medication, Notification, Mood, CBTExercise, CBTProgress
from datetime import datetime, timedelta
from django.http import JsonResponse
import cv2
import numpy as np
from deepface import DeepFace
import calendar
from datetime import date
from django.utils.safestring import mark_safe


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



@login_required
def health_tracker(request):
    if request.method == "POST":
        weight = request.POST.get("weight")
        sleep_hours = request.POST.get("sleep_hours")
        exercise_duration = request.POST.get("exercise_duration")
        HealthMetric.objects.create(
            user=request.user,
            weight=weight,
            sleep_hours=sleep_hours,
            exercise_duration=exercise_duration,
        )
        Notification.objects.create(
            user=request.user, content="Health metrics updated successfully!"
        )
        return redirect("health_tracker")
    metrics = HealthMetric.objects.filter(user=request.user).order_by("-date")
    return render(request, "health_tracker.html", {"metrics": metrics})


@login_required
def appointments(request):
    if request.method == "POST":
        doctor_name = request.POST.get("doctor_name")
        date = request.POST.get("date")
        time = request.POST.get("time")
        location = request.POST.get("location")
        reason = request.POST.get("reason")
        Appointment.objects.create(
            user=request.user,
            doctor_name=doctor_name,
            date=date,
            time=time,
            location=location,
            reason=reason,
        )
        Notification.objects.create(
            user=request.user, content=f"Appointment with {doctor_name} added."
        )
        return redirect("appointments")
    appointments = Appointment.objects.filter(user=request.user).order_by("date")
    return render(request, "appointments.html", {"appointments": appointments})


@login_required
def medications(request):
    if request.method == "POST":
        name = request.POST.get("name")
        dosage = request.POST.get("dosage")
        schedule_time = request.POST.get("schedule_time")
        notes = request.POST.get("notes")
        Medication.objects.create(
            user=request.user,
            name=name,
            dosage=dosage,
            schedule_time=schedule_time,
            notes=notes,
        )
        Notification.objects.create(
            user=request.user, content=f"Medication {name} added to your schedule."
        )
        return redirect("medications")
    medications = Medication.objects.filter(user=request.user)
    return render(request, "medications.html", {"medications": medications})


@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by(
        "-created_at"
    )
    return render(request, "notifications.html", {"notifications": notifications})

@login_required
def mini_games(request):
    return render(request, 'mini_games.html')

@login_required
def meditation_exercise(request):
    return render(request, 'meditation_exercise.html')


@login_required
def Selfcare(request):
    return render(request, 'Selfcare.html')

@login_required
def skill_building_exercises(request):
    return render(request, 'skill_building_exercises.html')


def detect_mood(request):
    if request.method == "POST" and request.is_ajax():
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        if not ret:
            return JsonResponse({'error': 'Unable to access camera.'}, status=400)

        # Save or process the image frame for analysis
        try:
            analysis = DeepFace.analyze(frame, actions=['emotion'])
            mood = analysis['dominant_emotion']
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

        # Store in database
        date_today = datetime.date.today()
        mood_entry, created = Mood.objects.get_or_create(user=request.user, date=date_today)

        # Save mood based on time of day
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            mood_entry.morning_mood = mood
        else:
            mood_entry.evening_mood = mood

        mood_entry.save()

        video_capture.release()
        return JsonResponse({'mood': mood})
    return JsonResponse({'error': 'Invalid request.'}, status=400)


@login_required
def mood_calendar(request):
    # Ensure the user is logged in
    moods = Mood.objects.filter(user=request.user)
    mood_dict = {m.date: {"morning": m.morning_mood, "evening": m.evening_mood} for m in moods}

    today = date.today()
    calendar_html = "<table class='calendar'>"
    calendar_html += "<tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>"

    c = calendar.Calendar()
    for week in c.monthdatescalendar(today.year, today.month):
        calendar_html += "<tr>"
        for day in week:
            if day.month == today.month:
                mood = mood_dict.get(day, {})
                morning = mood.get("morning", "🙂")
                evening = mood.get("evening", "🙂")
                calendar_html += f"<td>{day.day}<br>{morning} {evening}</td>"
            else:
                calendar_html += "<td></td>"
        calendar_html += "</tr>"

    calendar_html += "</table>"
    return render(request, "mood_calendar.html", {"calendar_html": mark_safe(calendar_html)})