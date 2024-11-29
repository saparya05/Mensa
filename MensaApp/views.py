from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomSignupForm, CustomLoginForm
from .models import DiaryEntry ,HealthMetric, Appointment, Medication, Notification
from datetime import datetime, timedelta


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
