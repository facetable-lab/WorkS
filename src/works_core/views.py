from django.shortcuts import render

from .models import Vacancy


# Функция отображения главной страницы
def home_view(request):
    vacancy_all = Vacancy.objects.all()
    context = {
        'vacancy_all': vacancy_all
    }
    return render(request, 'home.html', context)
