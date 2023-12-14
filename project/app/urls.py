from django.urls import path
from .views import index,order,create

urlpatterns = [
    path('',index,name='home'),
    path('orders',order,name='order'),
    path('create',create,name='create')
]