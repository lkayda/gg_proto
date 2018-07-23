from django.contrib import admin
from .models import (Tariff, Lesson, Schedule, ScheduleTimeValue)


admin.site.register(Tariff)
admin.site.register(Lesson)
admin.site.register(Schedule)
admin.site.register(ScheduleTimeValue)
