#from django.urls import path
#from . import views

#urlpatterns = [
  #  path('', views.home, name='home'),
  #  path('register/', views.register, name='register'),
   # path('get_branches/<str:district>/', views.get_branches, name='get_branches'),
  #  path('wikipedia/<str:district>/', views.wikipedia_redirect, name='wikipedia'),

from django.urls import path
from . import views
app_name = 'banking_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_registration, name='user_registration'),
    path('user-profile/', views.user_profile_form, name='user_profile_form'),

]

