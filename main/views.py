from django.shortcuts import render
from pytils.translit import slugify
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from main.models import Client, Mailing


# Create your views here.
class MailingListView(ListView):
    model = Mailing
    template_name = 'main/index.html'


class MailingCreateView(CreateView):
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

    model = Mailing
    success_url = reverse_lazy('index')


def mailinglogs(request):
    return render(request, 'main/mailinglogs.html')


def message(request):
    return render(request, 'main/message.html')


def client(request):
    return render(request, 'main/client.html')



