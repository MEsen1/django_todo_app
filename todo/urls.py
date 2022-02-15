from unicodedata import name
from django.urls import path
from .views import home, todo_list,todo_add,todo_update

urlpatterns = [
    path('',home, name='home'),
    path('todos/',todo_list,name='todo_list'),
    path('todo_add/',todo_add,name='todo_add'),
    path('todo_update/<int:id>/',todo_update,name='todo_update'),
]
