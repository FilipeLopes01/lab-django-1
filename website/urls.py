from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('temporada2021', views.temporada2021, name='temporada2021'),
    path('piloto1', views.piloto1, name='piloto1'),
    path('piloto2', views.piloto2, name='piloto2')
]