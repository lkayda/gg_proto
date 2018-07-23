from django.db import models

from games.models import Game
from users.models import (CoachProfile, GamerProfile)


class Tariff(models.Model):
    TARIFF_TYPE_CHOICES = (
        ('TRL', 'Trial'),
        ('LSS', 'Lesson'),
        ('PCK', 'Lessons Pack'),
        ('OTH', 'Other'),
    )

    name = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )
    tariff_type = models.CharField(
        max_length=3,
        choices=TARIFF_TYPE_CHOICES,
        null=False,
        blank=False
    )
    duration = models.IntegerField(
        blank=False,
        default=30
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )


class Lesson(models.Model):
    tariff = models.OneToOneField(
        Tariff,
        on_delete=models.CASCADE,
        primary_key=False
    )


class Schedule(models.Model):
    schedule_type = models.CharField(
        max_length=3
    )
    time_part_size = models.IntegerField(
        blank=False,
        default=30
    )
    coach_profile = models.ForeignKey(
        CoachProfile,
        on_delete=models.CASCADE
    )


class ScheduleTimeValue(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE
    )
    lesson = models.OneToOneField(
        Lesson,
        on_delete=models.CASCADE,
        primary_key=False,
        null=True,
        blank=True
    )
    datetime_value = models.DateTimeField(
        blank=False
    )
    is_taken = models.BooleanField()
    is_approved = models.BooleanField()
    is_completed = models.BooleanField()
    gamer = models.ForeignKey(
        GamerProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    coach = models.ForeignKey(
        CoachProfile,
        on_delete=models.CASCADE
    )
