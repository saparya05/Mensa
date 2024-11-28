from django.db import models
from django.contrib.auth.models import User

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link entry to a user
    title = models.CharField(max_length=200, blank=True, null=True)  # Optional title
    content = models.TextField()  # Diary content
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update on edit

    def __str__(self):
        return f"{self.user.username} - {self.title or 'No Title'}"
