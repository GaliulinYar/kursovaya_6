from django.urls import path
from . import views
from .views import ClientListView, mailing, mailinglogs, message, client

# from main.views import

urlpatterns = [
    path('', ClientListView.as_view(),  name='index'),
    path('mailing/', mailing),
    path('mailinglogs/', mailinglogs),
    path('message/', message),
    path('client/', client),

    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    # path('great_prod/', great_prod)
]