from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from django.views.generic.base import ContextMixin
from django.urls import reverse, reverse_lazy
from .models import Position, Vacancy
from .forms import FoundForm, MainForm
from .management.commands.datapars import Command


class MainView(FormView):
    template_name = 'pars/main.html'
    form_class = MainForm


class ParsResultView(ListView):
    model = Vacancy
    template_name = 'pars/results.html'
    paginate_by = 5

    def get_queryset(self):
        return Vacancy.objects.all().order_by('-id')[:20]


class FoundMixin(ContextMixin):
    def post(self, request, *args, **kwargs):
        found = request.POST['name']
        com = Command(found)
        com.handle()
        return HttpResponseRedirect(reverse('pars:results'))
        # return super().post(request,*args,**kwargs)

    def get(self, request, *args, **kwargs):
        form = FoundForm()
        return render(request, 'pars/found.html', context={'form': form})
        # form = FoundForm()
        # return super().get(request, *args, **kwargs)


class ParsFoundView(LoginRequiredMixin,CreateView, FoundMixin):
    template_name = 'pars/found.html'


class PsihView(TemplateView):
    template_name = 'pars/psih.html'
