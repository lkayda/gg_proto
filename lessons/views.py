from django.shortcuts import render
from rest_framework import viewsets
from lessons.api.serializers import (TariffSerializer, LessonSerializer, ScheduleSerializer, ScheduleTimingSerializer)
from lessons.models import Tariff, Lesson, Schedule, ScheduleTimeValue


class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleTimingViewSet(viewsets.ModelViewSet):
    queryset = ScheduleTimeValue.objects.all()
    serializer_class = ScheduleTimingSerializer
