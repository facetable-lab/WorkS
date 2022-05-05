from django import forms

from works_core.models import City, Specialization


# Класс формы поиска
class FindForm(forms.Form):
    # Инпут города
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='slug', required=False,
                                  widget=forms.Select(attrs={
                                      'class': 'form-control'
                                  }), label='Город')
    # Инпут Специализации (ЯП)
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all(), to_field_name='slug', required=False,
                                            widget=forms.Select(attrs={
                                                'class': 'form-control'
                                            }), label='Специальность')
