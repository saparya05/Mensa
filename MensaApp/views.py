from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomSignupForm, CustomLoginForm
from .models import DiaryEntry


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
