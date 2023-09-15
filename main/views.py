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

    def get_queryset(self):
        return Mailing.objects.all()


class MailingCreateView(CreateView):
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


class MailingDeleteView(DeleteView):
    """Класс для удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('index')


class MailingUpdateView(UpdateView):
    """Класс для изменения рассылки"""
    model = Mailing
    fields = ('name_mailing', 'theme_mess', 'body_mess', 'frequency', 'send_time')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name_mailing)
            new_mat.save()

        return super().form_valid(form)


def mailinglogs(request):
    return render(request, 'main/mailinglogs.html')


class ClientListView(ListView):
    model = Client
    template_name = 'main/client.html'


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('mail_client', 'name_client', 'first_name_client', 'last_name_client')
    success_url = reverse_lazy('client')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.mail_client)
            new_mat.save()

        return super().form_valid(form)


class ClientCreateView(CreateView):
    model = Client
    fields = ('mail_client', 'name_client', 'first_name_client', 'last_name_client')
    success_url = reverse_lazy('client')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.mail_client)
            new_mat.save()

        return super().form_valid(form)
