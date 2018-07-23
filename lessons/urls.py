from django.conf.urls import url, include
from rest_framework import routers
from lessons import views


router = routers.DefaultRouter()
router.register(r'tariffs', views.TariffViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'schedules', views.ScheduleViewSet)
router.register(r'schedule_timings', views.ScheduleTimingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
