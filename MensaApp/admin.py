from django.contrib import admin
from .models import DiaryEntry, HealthMetric, Appointment, Medication, Notification, Mood, CBTExercise, CBTProgress

@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')  # Fields to display
    search_fields = ('title', 'content')           # Search functionality
    list_filter = ('created_at', 'user')           # Filtering options


admin.site.register(HealthMetric)
admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(Notification)

admin.site.register(Mood)
admin.site.register(CBTExercise)
admin.site.register(CBTProgress)