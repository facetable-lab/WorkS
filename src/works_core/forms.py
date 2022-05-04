from django import forms

from works_core.models import City, Specialization


class FindForm(forms.Form):
   city = forms.ModelChoiceField(queryset=City.objects.all())
   specialization = forms.ModelChoiceField(queryset=Specialization.objects.all())
