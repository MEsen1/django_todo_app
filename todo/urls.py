from unicodedata import name
from django.urls import path
from .views import home, todo_list,todo_add,todo_update,todo_delete,todo_detail

urlpatterns = [
    path('',home, name='home'),
    path('todos/',todo_list,name='todo_list'),
    path('todo_add/',todo_add,name='todo_add'),
    path('todo_detail/<int:id>/',todo_detail,name='todo_detail'), 
    path('todo_update/<int:id>/',todo_update,name='todo_update'),
    path('todo_delete/<int:id>/',todo_delete,name='todo_delete'),
]
