from .models import Edu_Service

def get_first_service_id(request):
    ''' 
        Bu context processoru əlave etdim ki, layout.html də ən birinci
        service ID-ni götürək
        1, 2 yaza bilərdim amma əgər İD 1 ilə service silinsə onda error olacaqdı.
    '''
    return {
        'first_service_id': Edu_Service.objects.first().id
    }
