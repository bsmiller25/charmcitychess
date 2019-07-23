from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/<gal_str>', views.gallery, name='gallery'),
    path('bylaws/', views.bylaws, name='bylaws'),
]
