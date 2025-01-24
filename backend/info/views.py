from django.shortcuts import render
from .models import Edu_Service


# Create your views here.
def service(request, pk):
    detail = Edu_Service.objects.get(id=pk)
    all_services = Edu_Service.objects.all()
    ctx = {
        "all_services": all_services,
        "detail": detail,
    }
    return render(request, "service.html", ctx)
