from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('gallery/<gal_str>', views.gallery, name='gallery'),
    path('bylaws/', views.bylaws, name='bylaws'),
    path('new_tournament/', views.new_tournament, name='new_tournament'),
]
 
