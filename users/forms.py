from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# # Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
 
    class Meta:
        model = Profile
        fields = ['image']

# class ProfileUpdateDetails(forms.ModelForm):

#     ENGINEERING_CHOICES = (
#         ('data', 'Data'),
#         ('electronics', 'Electronics'),
#         ('electrical', 'Electrical'),
#     )
#     STUDIO_LEVEL_CHOICES = (
#         ('fundamentals a', 'Fundamentals A'),
#         ('fundamentals b', 'Fundamentals B'),
#         ('applications a', 'Applications A'),
#         ('applications b', 'Applications B'),
#         ('professionals a', 'Professionals A'),
#         ('professionals b', 'Professionals B'),
#     )
#     GRADE_CHOICES = (
#         ('p', 'P'),
#         ('c', 'C'),
#         ('d', 'D'),
#         ('hd', 'HD'),
#     )
    

#     engineering_discipline = forms.ChoiceField(choices=ENGINEERING_CHOICES, required=False)
#     # engineering_discipline = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 12}), required=False)
#     student_id_number = forms.IntegerField(required=False)
#     student_first_name = forms.CharField(max_length=255, required=False)
#     student_last_name = forms.CharField(max_length=255, required=False)
#     studio_level = forms.ChoiceField(choices=STUDIO_LEVEL_CHOICES, required=False)
#     student_year = forms.IntegerField()
#     on_campus = forms.BooleanField()
#     desired_grade = forms.ChoiceField(choices=GRADE_CHOICES, required=False)


#     class Meta:
#         model = Profile
#         fields = ['engineering_discipline', 'student_id_number', 'student_first_name', 'student_last_name', 
#                   'studio_level', 'student_year', 'on_campus', 'desired_grade']
