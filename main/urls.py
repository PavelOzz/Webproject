from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= 'home'),
    path('about-us',views.about, name='about'),
    path('svyaz',views.obratnaya_svyaz, name='svyaz'),
    path('Menu',views.menu_home, name='menu')
]