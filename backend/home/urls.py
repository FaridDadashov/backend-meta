from django.urls import path
from . import views
app_name='home'

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('values/',views.values,name="values"),
    path('team/',views.team,name="team"),
    path('blog',views.blog,name="blog"),
    path('team/<int:pk>/', views.team_id, name="team_id"),
    path('blog-detail/<int:pk>', views.blog_detail, name='blog_detail')
    

    
]

