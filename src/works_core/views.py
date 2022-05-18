from django.core.paginator import Paginator
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

    page_obj = []
    if city or specialization:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if specialization:
            _filter['specialization__slug'] = specialization

        vacancy_all = Vacancy.objects.filter(**_filter)

        #     Пагинация
        paginator = Paginator(vacancy_all, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {
        'vacancy_all': page_obj,
        'form': form
    }
    return render(request, 'works_core/list.html', context)
