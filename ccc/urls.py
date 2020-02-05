from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    #path('accounts/password_reset/', auth_views.LoginView.as_view(template_name='registration/password_reset_form.html')),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/register/', views.register, name='register'),
    path('members/', views.members, name='members'),
    path('coaching/', views.coaching, name='coaching'),
    path('gallery/<gal_str>', views.gallery, name='gallery'),
    path('bylaws/', views.bylaws, name='bylaws'),
    path('new_tournament/', views.new_tournament, name='new_tournament'),
]
 
