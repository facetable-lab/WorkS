from django.shortcuts import render
import datetime


# Функция отображение главной страницы
def home(request):
    date_now = datetime.datetime.now().date()
    title = 'Home page'
    _context = {
        'date_now': date_now,
        'title': title
    }
    return render(request, 'home.html', _context)
