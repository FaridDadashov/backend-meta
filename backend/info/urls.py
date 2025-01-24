from django.urls import path
from . import views
app_name='info'

urlpatterns = [
    path('service/<int:pk>',views.service,name="service"),
]

