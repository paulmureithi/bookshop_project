from django.urls import path
from .views import OrderPageView, charge

urlpatterns = [
    path('charge/', charge, name='charges'),
    path('', OrderPageView.as_view(), name='orders'),
]