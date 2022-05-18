from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


# Функция отображения главной страницы
def home_view(request):
    form = FindForm()
    return render(request, 'works_core/home.html', {'form': form})


# Функция отображения списка вакансий
def list_view(request):
    city = request.GET.get('city')
    specialization = request.GET.get('specialization')
    form = FindForm()

    vacancy_all = []
    if city or specialization:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if specialization:
            _filter['specialization__slug'] = specialization

        vacancy_all = Vacancy.objects.filter(**_filter)

    context = {
        'vacancy_all': vacancy_all,
        'form': form
    }
    return render(request, 'works_core/list.html', context)
