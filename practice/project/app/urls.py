from django.db import path
from . import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('new/',views.new1, name='xyz')
]