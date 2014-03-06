from django.db import models
from django.contrib.auth.models import User

class ProgramPart(models.Model):
    PILLARS = (
        ('know','Learning to Know'),
        ('do','Learning to Do'),
        ('live','Learning to Live Together'),
        ('be','Learning to Be'),
    )

    length = models.IntegerField(null=True, help_text="Length in minutes")
    camper_action = models.TextField(blank=True)
    volunteer_action = models.TextField(blank=True)
    pillar_of_education = models.CharField(max_length=4, choices=PILLARS, blank=True, null=True)

class Indicator(models.Model):
    OBSERVATION_LEVELS = (
        (0, "Not observed"),
        (1, "Partially observed"),
        (2, "Mostly observed"),
        (3, "Observed"),
        (4, "Other"),
    )
    indicator_name = models.TextField(blank=True)
    measurement = models.TextField(blank=True, help_text="e.g. X%, Y mins")
    observation = models.IntegerField(blank=True, choices=OBSERVATION_LEVELS, null=True)
    observation_other = models.TextField(blank=True, help_text="Explain if other observation")

class Approach(models.Model):
    approach_name = models.TextField(blank=False)

class LifeSkill(models.Model):
    skill_name = models.TextField(blank=False)

class Session(models.Model):
    lship = models.ManyToManyField(User, null=True, blank=False)
    year = models.IntegerField(blank=False)
    name = models.TextField(blank=False)

class Program(models.Model):
    # Program info
    volunteers = models.ManyToManyField(User, null=True)
    title = models.TextField(blank=False)
    summary = models.TextField(blank=True)
    session = models.ManyToManyField(Session, blank=True)
    day_theme = models.TextField(blank=True)
    day = models.TextField(blank=True)
    unit_specialty = models.TextField(blank=True)
    time_of_day = models.TextField(blank=True)

    # Core concepts
    core_concepts = models.TextField(blank=True)
    desired_outcomes = models.TextField(blank=True)

    # Program details
    parts = models.ManyToManyField(ProgramPart, blank=True, null=True)
    debrief = models.TextField(blank=True)
    indicators = models.ManyToManyField(Indicator, blank=True, null=True)
    resources = models.TextField(blank=True)
    location = models.TextField(blank=True)
    prep = models.TextField(blank=True)
    support = models.TextField(blank=True)

    # Post-eval
    approach = models.ManyToManyField(Approach, blank=True, null=True)
    life_skills = models.ManyToManyField(LifeSkill, blank=True, null=True)
    followup = models.TextField(blank=True)
    met_outcomes = models.TextField(blank=True) # Do indicators show outcomes were met?
    adjustments = models.TextField(blank=True)

