from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView

import random

from .models import ListNames
from .forms import ListNamesForm


class ListNamesView(ListView):
    form_class = ListNamesForm
    template_name = 'list.html'
    model = ListNames
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super(ListNamesView, self).get_context_data(**kwargs)
        context['form'] = self.form_class

        count = 3
        qs_count = self.model.objects.count()
        if qs_count < 3:
        	count = qs_count
        context['winner_list'] = random.sample([name for name in self.model.objects.all()], k=count)
        
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('names:list'))
        return render(
                request,
                self.template_name,
                {self.context_object_name: self.get_queryset(), 'form': form}
                )


class ListNamesDelete(DeleteView):
    model = ListNames
    success_url = reverse_lazy('names:list')


class WinnerView(ListView):
    template_name = 'winners.html'
    model = ListNames

    def get_context_data(self, **kwargs):
        context = super(WinnerView, self).get_context_data(**kwargs)

        count = 3
        qs_count = self.model.objects.count()
        if qs_count < 3:
        	count = qs_count
        context['winner_list'] = random.sample([name for name in self.model.objects.all()], k=count)
        
        return context
