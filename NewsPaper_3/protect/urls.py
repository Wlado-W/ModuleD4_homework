from django.urls import path
from . import views

app_name = 'protect'

urlpatterns = [
    path('protected/', views.protected_view, name='protected_view'),
]
