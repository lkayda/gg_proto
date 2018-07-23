from django.contrib import admin
from .models import (User, GamerProfile, CoachProfile)


admin.site.register(User)
admin.site.register(GamerProfile)
admin.site.register(CoachProfile)
