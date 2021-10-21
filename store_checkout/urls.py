from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_done/<order_number>', views.checkout_done, name='checkout_done'),
    path('wh/', webook, name='webhook'),
]
