import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from database.models import *

admin = User.objects.create_user(username='admin', first_name='Admin', last_name='Admin', email='admin@gmail.com', password='admin')
admin.is_superuser = True
admin.is_staff = True
admin.save()

skills = [
    ['rapping', 'rapp', 'https://media.istockphoto.com/id/1160768128/photo/rap-musician-in-studio.jpg?s=612x612&w=0&k=20&c=8LzuLliur66CaZnXywhBZzcTRellYlRF3gRCTlSG3XE='],
    ['pottery', 'pttr', 'https://www.outlookindia.com/outlooktraveller/public/uploads/articles/explore/header6.jpg'],
    ['poetry', 'poet', 'https://images.unsplash.com/photo-1473186505569-9c61870c11f9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cG9ldHJ5fGVufDB8fDB8fA%3D%3D&w=1000&q=80'],
    ['makeup', 'makp', 'https://img5.goodfon.com/wallpaper/nbig/0/94/makeup-artist-woman-makeup.jpg'],
    ['modelling', 'modl', 'https://wallpapers.com/images/hd/aesthetic-bts-jin-phone-modelling-tnbwrfcb0q2lmtuu.jpg'],
    ['beatboxing', 'btbx', 'https://static.wikia.nocookie.net/beatbox/images/b/bb/NaPoM_GBB_2021.jpg'],
]

for skill in skills:
    Skill(
        name = skill[0],
        slug = skill[1],
        image = skill[2],
        count = 0
    ).save()

events = [
    ['rapping', 'https://cdn.telanganatoday.com/wp-content/uploads/2023/01/Pot.jpg'],
    ['pottery', 'https://imgstaticcontent.lbb.in/lbbnew/wp-content/uploads/2018/03/28214729/hyderabadpoetryproject3.jpg'],
    ['poetry', 'https://d3emaq2p21aram.cloudfront.net/media/cache/venue_roundup_single_image/uploads/TheVenueReport-Beauty101-AlissaNoelle-08.jpg'],
    ['makeup', 'https://blog.ipleaders.in/wp-content/uploads/2021/05/How-do-you-organize-a-Runway-Fashion-Show-1.jpg'],
    ['modelling', 'https://wallpapers.com/images/hd/aesthetic-bts-jin-phone-modelling-tnbwrfcb0q2lmtuu.jpg'],
    ['beatboxing', 'https://www.musicianwave.com/wp-content/uploads/2022/02/How-to-Rap-Fast-788x525.jpg'],
]

for event in events:
    Event(
        name = f'{event[0].capitalize()} Competition',
        organizer = admin,
        image = event[1]
    ).save()