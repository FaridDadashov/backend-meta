from django.contrib import admin
from django.urls import path

from . import views as vacancies_views

urlpatterns = [
    path('', vacancies_views.vacancy_view, name='vacancy'),
    path('detail/<uuid:uuid>/', vacancies_views.vacancy_detail, name='vacancy_detail'),
    path('search/', vacancies_views.search, name='search'),
]
