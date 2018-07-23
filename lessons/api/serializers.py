from rest_framework import serializers
from lessons.models import Tariff, Lesson, Schedule, ScheduleTimeValue


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleTimeValue
        fields = '__all__'
