from django.shortcuts import render,get_object_or_404
from .models import Team,Blog

# Create your views here.

def home(request):
    
    teams=Team.objects.all()[:4]
    return render(request,'home.html',{'teams':teams})

def about(request):
    return render(request,'about.html')


def values(request):
    return render(request,'values.html')

def team(request):
    teams=Team.objects.all()
        
    return render(request,'team.html',{
        'teams':teams  
        
    })
    

def team_id(request, pk):
    teams = Team.objects.all()[:4]
    team = get_object_or_404(Team, pk=pk) 
    return render(request, 'teamid.html', {'team': team,'teams':teams})



def blog(request):
    blogs=Blog.objects.all()
    return render(request,'blog.html',{'blogs':blogs})

def blog_detail(request, pk):
    blogs=Blog.objects.all()[:4]
    blog = get_object_or_404(Blog, pk=pk)  
    return render(request, 'blog-detail.html', {'blog': blog,'blogs':blogs})
