from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView, TemplateView

from main.forms import ClientForm, MailingForm
from main.models import Client, Mailing


class HomeView(TemplateView):
    template_name = 'main/home.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:client_list')


class ClientListView(ListView):
    model = Client
    template_name = 'main/client_list.html'


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = 'main:mailing_list'


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = 'main:mailing_detail'


class MailingDeleteView(DeleteView):
    model = Mailing
    form_class = MailingForm
    success_url = 'main:mailing_list'


class MailingListView(ListView):
    model = Mailing
    template_name = 'main/mailing_list.html'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'main/mailing_detail.html'
