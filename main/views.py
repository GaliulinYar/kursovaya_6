from django.shortcuts import render
from django.views.generic import ListView
from main.models import Client


# Create your views here.
class ClientListView(ListView):
    model = Client
    template_name = 'main/index.html'

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(publ_on_off=True)
    #     return queryset
