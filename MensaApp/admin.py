from django.contrib import admin
from .models import DiaryEntry

@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')  # Fields to display
    search_fields = ('title', 'content')           # Search functionality
    list_filter = ('created_at', 'user')           # Filtering options
