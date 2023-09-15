from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views
from .views import MailingListView, mailinglogs, message, client, MailingCreateView, MailingDeleteView

# from main.views import

urlpatterns = [
    path('', MailingListView.as_view(),  name='index'),
    path('mailinglogs/', mailinglogs),
    path('message/', message),
    path('client/', client),

    path('create/', MailingCreateView.as_view(), name='create_product'),
    #path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),

    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    # path('great_prod/', great_prod)
]