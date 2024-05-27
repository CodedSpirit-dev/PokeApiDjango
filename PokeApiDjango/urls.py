"""
URL configuration for PokeApiDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemon/fetch/<str:pokemon_name_or_id>/', fetch_pokemon_data),
    path('pokemon/add_custom/', add_custom_pokemon_data),
    path('pokemon/update/<str:pokemon_name_or_id>/', update_pokemon_data_in_db),
    path('pokemon/delete/<str:pokemon_name_or_id>/', delete_pokemon_data_in_db),
    path('pokemon/get/<str:pokemon_name_or_id>/', get_pokemon_data_from_db),
    path('list_all/', get_list_of_pokemon_saved_in_db),
    path('pokemon/calculate_score/<str:pokemon_name_or_id>/', calculate_pokemon_score),
]
