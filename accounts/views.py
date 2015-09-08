from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms


def register(request):
    form = forms.RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'accounts/register.html', {'form': form})
