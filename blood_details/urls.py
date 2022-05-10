from django.urls import path
from .views import add_donor, all_donor

app_name = 'accounts'

urlpatterns = [
    path('', all_donor, name="list_donor"),
    path('add/', add_donor, name='add_donor'),
]
