from .models import Edu_Service

def get_first_service_id(request):
    ''' 
        Bu context processoru əlave etdim ki, layout.html də ən birinci
        service ID-ni götürək
        1, 2 yaza bilərdim amma əgər İD 1 ilə service silinsə onda error olacaqdı.
    '''
    first_obj = Edu_Service.objects.first()
    first_id = 0
    if first_obj is not None:
        first_id = Edu_Service.objects.first().id
    return {
        'first_service_id': first_id
    }
