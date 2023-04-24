from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.College)
admin.site.register(models.Skill)
admin.site.register(models.Event)
admin.site.register(models.EventParticipant)
admin.site.register(models.Collab)