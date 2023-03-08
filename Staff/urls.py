from django.urls import path
from Staff.views import inicio, index, index_dos

urlpatterns = [
    path('', inicio),
    path('index/', index),
    path('index_2/', index_dos),
]
