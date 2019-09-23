from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from monitor.models import Crn
from django.urls import reverse_lazy

from django.template.response import TemplateResponse
from django.utils import timezone

from django.views import generic
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from monitor.forms import CrnForm
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)

from django.http.response import HttpResponse
from monitor.models import Crn
from datetime import datetime
from .filters import CRNFilter
from django_filters import DateFromToRangeFilter
from django.views import View
from braces.views import SelectRelatedMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




@method_decorator(login_required, name='dispatch')
class CrnListView(LoginRequiredMixin,generic.ListView):

    model = Crn

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CRNFilter(self.request.GET, queryset=self.get_queryset())
        return context

    # def get_queryset(self):
    #     return Crn.objects.filter(created_at__lte=datetime.now()).order_by('-created_at')

@method_decorator(login_required, name='dispatch')
class CrnDetailView(LoginRequiredMixin,generic.DetailView):
    model = Crn


@method_decorator(login_required, name='dispatch')
class CreateCrnView(LoginRequiredMixin,generic.CreateView):
    login_url = '/login'
    redirect_field_name = 'monitor/crn_detail.html'
    form_class = CrnForm
    model = Crn


@method_decorator(login_required, name='dispatch')
class CrnUpdateView(LoginRequiredMixin,generic.UpdateView):
    login_url = '/login'
    redirect_field_name = 'monitor/crn_detail.html'
    form_class = CrnForm
    model = Crn

@method_decorator(login_required, name='dispatch')
class CrnDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Crn
    success_url = reverse_lazy('crn_list')


# class SearchView(LoginRequiredMixin,View):

#     model = Crn
#     queryset_list = Crn.objects.all()
#     template_name = 'monitor/search.html'

#     def get_context_data(request, self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = CRNFilter(self.request.GET, queryset=self.get_queryset())
#         #return context

#         args = {'context': context}

#         return render(request, self.template_name ,args)

@login_required
def allcrn(request):
    queryset_list = Crn.objects.order_by('-created_at')

    context = {
        
        'crns': queryset_list ,
        
    }

    return render(request, 'monitor/allcrn.html' ,context)