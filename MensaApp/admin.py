from django.contrib import admin
from .models import DiaryEntry, HealthMetric, Appointment, Medication, Notification, CBTExercise, CBTProgress

@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')  
    search_fields = ('title', 'content')           
    list_filter = ('created_at', 'user')           

admin.site.register(HealthMetric)
admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(Notification)
admin.site.register(CBTExercise)
admin.site.register(CBTProgress)