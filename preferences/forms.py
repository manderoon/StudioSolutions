from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Preferences
from products.models import Product
from django.forms import ModelChoiceField

# class PreferencesChoiceField(forms.ModelChoiceField):
#         def label_from_instance(self, obj):
#             return obj.name

# class PreferencesUpdateForm(forms.Form):
#     p1 = PreferencesChoiceField(queryset=Product.objects.all(), label='1st Preference')
#     p2 = PreferencesChoiceField(queryset=Product.objects.all(), label='2nd Preference', required=False)
#     p3 = PreferencesChoiceField(queryset=Product.objects.all(), label='3rd Preference', required=False)

    

#     class Meta:
#         model = Preferences
#         fields = ['p1', 'p2', 'p3']       

class PreferencesForm(forms.ModelForm):
        
    first_pref = forms.ModelChoiceField(queryset=Product.objects.all(), to_field_name='id', label = 'First Preference')
    second_pref = forms.ModelChoiceField(queryset=Product.objects.all(), to_field_name='id', required=False)
    third_pref = forms.ModelChoiceField(queryset=Product.objects.all(), to_field_name='id', required=False)

    class Meta:
        model = Preferences
        fields = ('first_pref', 'second_pref', 'third_pref')