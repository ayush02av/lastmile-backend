from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    sub = models.CharField(max_length=100)
    sid = models.CharField(max_length=100)
    interests = models.ManyToManyField(to="database.Skill", related_name="user_interests", blank=True)
    ratings = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.username}"

class College(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=6, unique=True)
    pincode = models.IntegerField()

    def __str__(self):
        return f"{self.slug}-{self.pincode}"

class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=6, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.slug}-{self.count}"

class Event(models.Model):
    name = models.CharField(max_length=255)
    organizer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='event_organizer')
    venue_options = models.JSONField(default=list, blank=True)
    venue = models.JSONField(default=dict, blank=True)
    category = models.ForeignKey(to=Skill, related_name="event_category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class EventParticipant(models.Model):
    event = models.ForeignKey(to=Event, related_name='evenparticipant_event', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='eventparticipant', on_delete=models.CASCADE)
    vote = models.JSONField(default=dict, blank=True)
    rating = models.IntegerField(default=0)
    
class Collab(models.Model):
    from_user = models.ForeignKey(to=User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(to=User, related_name='to_user', on_delete=models.CASCADE)
    skill = models.ForeignKey(to=Skill, related_name='skill', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"From {self.from_user.__str__()} To {self.to_user.__str__()} For {self.skill.__str__()}"