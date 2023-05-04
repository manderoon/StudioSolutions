from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView
from .models import *


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products_list2.html'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "products/product_detail.html"

class ProductOwnerListView(ListView):
    model = ProductOwner
    context_object_name = 'productowners'
    template_name = "products/product_owners.html"

class ProductOwnerDetailView(DetailView):
    model = ProductOwner
    context_object_name = 'productowner'
    template_name = "products/product_owners_detail.html"


class SkillListView(ListView):
    model = Skill
    context_object_name = 'skills'
    template_name = "skills/skills_list.html"

class ActivitiesList(ListView):
    model = IlcActivity
    context_object_name = 'ilcactivities'
    template_name = "ilc/activities_list.html"

class StudentActivitiesList(ListView):
    model = StudentIlcActivity
    context_object_name = 'studentactivity'
    template_name = "ilc/studentactivities_list.html"


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddSkillForm, AddActivityForm, AddStudentActivityForm

@login_required
def addSkill(request):
    if request.method == 'POST':
        u_form = AddSkillForm(request.POST)
        if u_form.is_valid():
    
                skill = u_form.save(commit=False)
                skill.user = request.user
                skill.save()
                print(u_form)
                messages.success(request, f'The skill has been added!')
                return redirect('skills.list') # Redirect back to skill page
        else:
            print(f"Invalid form data: {u_form.errors}")
    else:
        u_form = AddSkillForm()

    context = {
        'u_form': u_form,
    }
    return render(request, 'skills/add_skill.html', context)

@login_required
def addActivity(request):
    if request.method == 'POST':
        u_form = AddActivityForm(request.POST)
        if u_form.is_valid():
    
                skill = u_form.save(commit=False)
                skill.user = request.user
                skill.save()
                print(u_form)
                messages.success(request, f'The activity has been added!')
                return redirect('activities.list') # Redirect back to skill page
        else:
            print(f"Invalid form data: {u_form.errors}")
    else:
        u_form = AddActivityForm()

    context = {
        'u_form': u_form,
    }
    return render(request, 'ilc/add_activity.html', context)

from django import forms
from django.contrib.auth.models import User
# class MyForm(forms.Form):
#     student = forms.CharField()

#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
#         if self.user:
#             self.fields['student'].initial = self.user.username

@login_required
def addStudentActivity(request):
    if request.method == 'POST':
        u_form = AddStudentActivityForm(request.POST)
        if u_form.is_valid():
            review = u_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'The activity review has been added!')
            return redirect('studentactivities.list')
        else:
            print(f"Invalid form data: {u_form.errors}")
    else:
        u_form = AddStudentActivityForm()

    context = {
        'u_form': u_form}
    return render(request, 'ilc/add_studentactivity.html', context)
