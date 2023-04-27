from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PreferencesForm
from .models import Preferences


@login_required
def preferences_view(request):
    if request.method == 'POST':
        form = PreferencesForm(request.POST)
        print(f"1.is this working {form} \n")
        if form.is_valid():
            preferences = form.save(commit=False)
            preferences.user = request.user
            #print("2.is this working" + form + "\n")
            preferences.save()
            #print("3.is this working" + form + "\n")
            messages.success(request, f'Your preferences have been updated!')
            return redirect('products.list')
    else:
        form = PreferencesForm()
        print(f"2.is this working {form} \n")
    return render(request, 'preferences/preferences.html', {'form': form})

# # Update it here
# @login_required
# def preferences(request):
#     preferences = Preferences.objects.get(user=request.user)  # Retrieve the preferences for the logged-in user

#     if request.method == 'POST':
#         u_form = PreferencesUpdateForm(request.POST, instance=preferences)  # Pass the preferences instance to the form
#         if u_form.is_valid():
#             u_form.save()  # Save the updated preferences

#             messages.success(request, f'Your preferences have been updated!')
#             return redirect('preferences')
#     else:
#         u_form = PreferencesUpdateForm(instance=preferences)  # Pass the preferences instance to the form

#     context = {
#         'u_form': u_form,
#     }

#     return render(request, 'preferences/preferences.html', context)