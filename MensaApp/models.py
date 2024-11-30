from django.db import models
from django.contrib.auth.models import User
from django.db import models
from datetime import time

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link entry to a user
    title = models.CharField(max_length=200, blank=True, null=True)  # Optional title
    content = models.TextField()  # Diary content
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update on edit

    def __str__(self):
        return f"{self.user.username} - {self.title or 'No Title'}"


class HealthMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField(null=True, blank=True)
    sleep_hours = models.FloatField(null=True, blank=True)
    exercise_duration = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Appointment with {self.doctor_name} on {self.date} at {self.time}"

class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    schedule_time = models.TimeField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.dosage} at {self.schedule_time}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.content}"

class CBTExercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    template = models.JSONField()  # Store templates like Thought Record

    def __str__(self):
        return self.title

class CBTProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(CBTExercise, on_delete=models.CASCADE)
    response = models.JSONField()  # Store user responses dynamically
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.title}"
    
class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    morning_mood = models.CharField(max_length=50, blank=True, null=True)
    evening_mood = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"