from django.shortcuts import render
from . models import Edu_Service

# Create your views here.
def service(request,pk):
    services=Edu_Service.objects.all()
    detail=Edu_Service.objects.get(id=pk) or services[:-1]
    return render (request,'service.html',{'service':services,'detail':detail})