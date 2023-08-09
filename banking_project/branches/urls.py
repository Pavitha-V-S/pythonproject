from django.urls import path
from . import views

app_name = 'branches'

urlpatterns = [
    path('districts-branches/', views.district_branches, name='district_branches'),

    path('districts/', views.district_list, name='district_list'),
    path('districts/<int:district_id>/', views.district_wikipedia, name='district_wikipedia'),
]


