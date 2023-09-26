from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from pytils.translit import slugify
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from main.models import Client, Mailing


# Create your views here.
class MailingListView(ListView):
    """Показывает все рассылки"""
    model = Mailing
    template_name = 'main/index.html'
    context_object_name = 'object'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if user.groups.filter(name='manager').exists() or user.is_superuser:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(
                mailing_owner=user.pk
            )
        return queryset


class MailingCreateView(CreateView, LoginRequiredMixin):
    """Класс для создания рассылки"""
    model = Mailing
    fields = ('name_mailing', 'theme_mess', 'body_mess', 'frequency', 'send_time')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name_mailing)
            new_mat.save()

        return super().form_valid(form)


class MailingDeleteView(DeleteView, LoginRequiredMixin):
    """Класс для удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('index')


class MailingUpdateView(UpdateView, LoginRequiredMixin):
    """Класс для изменения рассылки"""
    model = Mailing
    fields = ('status', 'name_mailing', 'theme_mess', 'body_mess', 'frequency', 'send_time', 'client')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name_mailing)
            new_mat.save()

        return super().form_valid(form)


def mailinglogs(request):
    return render(request, 'main/mailinglogs.html')


class ClientListView(ListView, LoginRequiredMixin):
    model = Client
    template_name = 'main/client.html'


class ClientDeleteView(DeleteView, LoginRequiredMixin):
    model = Client
    success_url = reverse_lazy('client')


class ClientUpdateView(UpdateView, LoginRequiredMixin):
    model = Client
    fields = ('mail_client', 'name_client', 'first_name_client', 'last_name_client')
    success_url = reverse_lazy('client')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.mail_client)
            new_mat.save()

        return super().form_valid(form)


class ClientCreateView(CreateView, LoginRequiredMixin):
    model = Client
    fields = ('mail_client', 'name_client', 'first_name_client', 'last_name_client')
    success_url = reverse_lazy('client')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.mail_client)
            new_mat.save()

        return super().form_valid(form)
