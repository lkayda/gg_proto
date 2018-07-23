from django.db import models


class User(models.Model):
    name = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )


class GamerProfile(models.Model):
    name = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )


class CoachProfile(models.Model):
    name = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )
