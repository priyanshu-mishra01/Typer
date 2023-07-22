from django.urls import path

from . import views



urlpatterns = [
    path('',views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('solo/', views.solo, name='solo'),
    path('multiplayer/', views.multiplayer, name='multiplayer'),
    # path('contacts/', include('contacts.urls')),

]

