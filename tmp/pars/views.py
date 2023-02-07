from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import Position, Vacancy
from .forms import FoundForm
from .management.commands.datapars import Command


def main_view(request):
    return render(request, 'pars/main.html', context={})


def result_view(request):
    vacancy = Vacancy.objects.all().order_by('-id')[:20]
    return render(request, 'pars/results.html', context={'vacancy': vacancy})


def found_view(request):
    if request.method == 'POST':
        form = FoundForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name']
            print(data)
            com = Command(data)
            com.handle()
            return HttpResponseRedirect(reverse('pars:results'))
        else:
            return render(request, 'pars/found.html', context={'form': form})
    else:
        form = FoundForm()
        return render(request, 'pars/found.html', context={'form': form})

# Create your views here.
