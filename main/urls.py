from django.urls import path
from . import views
from .views import ClientListView

# from main.views import

urlpatterns = [
    path('', ClientListView.as_view(),  name='index'),
    # path('contacts/', contacts),
    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    # path('great_prod/', great_prod)
]