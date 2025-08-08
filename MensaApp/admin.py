from django.contrib import admin
from .models import StaticPage, DiaryEntry, HealthMetric, Appointment, Medication, Notification, CBTExercise, CBTProgress

# Change the title text in the admin site
admin.site.site_header = "Mensa Admin"
admin.site.site_title = "Mensa Admin Portal"
admin.site.index_title = "Welcome to the Admin Dashboard"


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('page_key', 'title')


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