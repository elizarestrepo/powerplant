from django.conf.urls import url
from django.urls import path, include
from code_challenge.views import power_supply

urlpatterns = [
    path('productionplan', power_supply, name='power_supply'),
]