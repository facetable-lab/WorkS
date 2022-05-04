from django.shortcuts import render

from .models import Vacancy


# Функция отображения главной страницы
def home_view(request):
    city = request.GET.get('city')
    specialization = request.GET.get('specialization')

    vacancy_all = []
    if city or specialization:
        _filter = {}
        if city:
            _filter['city__name'] = city
        if specialization:
            _filter['specialization__name'] = specialization

        vacancy_all = Vacancy.objects.filter(**_filter)

    context = {
        'vacancy_all': vacancy_all
    }
    return render(request, 'works_core/home.html', context)
