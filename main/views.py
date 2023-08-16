from django.shortcuts import render
from django.views.generic import ListView
from main.models import Client


# Create your views here.
class ClientListView(ListView):
    model = Client
    template_name = 'main/index.html'


def mailing(request):
    return render(request, 'main/mailing.html')


def mailinglogs(request):
    return render(request, 'main/mailinglogs.html')


def message(request):
    return render(request, 'main/message.html')


def client(request):
    return render(request, 'main/client.html')



