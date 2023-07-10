from django.urls import path
from . import views

urlpatterns = [
    path('match/', views.say_hello),
    path('natch/savedb/', views.savedb, name="savedb")
    
]