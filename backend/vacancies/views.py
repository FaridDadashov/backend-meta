from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from django.utils.timezone import localtime

from .models import Category, Vacancy


def vacancy_view(request):
    vacancy = Vacancy.objects.first()
    created_at = localtime(vacancy.created_at)
    filter_option = request.GET.get("filter")

    # Get all categories
    categories = Category.objects.all()

    if filter_option is not None:
        # Get vacancies based on filter
        vacancies = Vacancy.objects.filter(category__category_name=filter_option)
        ctx = {"vacancies": vacancies, "categories": categories}
        return render(request, "vacancy.html", context=ctx)

    # Get all vacancies
    vacancies = Vacancy.objects.all()

    ctx = {"vacancies": vacancies, "categories": categories}
    return render(request, "vacancy.html", context=ctx)


def vacancy_detail(request, uuid):
    # Get all vacancies
    vacancy = Vacancy.objects.get(id=uuid)

    ctx = {"vacancy": vacancy}
    return render(request, "vacancy_detail.html", context=ctx)


def search(request):
    try:
        search_query = request.POST.get("search_query")
        category_query = request.POST.get("filter")

        if not category_query == '':
            vacancies = Vacancy.objects.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query),
                category__category_name=category_query,
            )
        else:
            vacancies = Vacancy.objects.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query),
            )
            
        ctx = {
            "vacancies": vacancies,
            "query_length": len(vacancies),
            "query_string": search_query,
        }
        return render(request, "search.html", context=ctx)
    except Exception:
        return HttpResponse("Error", 500)
