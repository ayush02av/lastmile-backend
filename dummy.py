import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from database.models import *

admin = User.objects.create_user(username='admin', first_name='Admin', last_name='Admin', email='admin@gmail.com', password='admin')
admin.is_superuser = True
admin.is_staff = True
admin.save()

skills = [
    ['Beatboxing', 'btbx'],
    ['Rapping', 'rapp'],
    ['Pottery', 'pttr'],
    ['Makeup', 'makp'],
    ['Modelling', 'modl'],
    ['Poetry', 'poet']
]

for skill in skills:
    Skill(
        name = skill[0],
        slug = skill[1],
        count = 0
    ).save()