from django.urls import path

from crudapp import views

urlpatterns = [
    path('', views.log_list, name='log_list'),
    path('view/<int:pk>', views.log_view, name='log_view'),
    path('new', views.log_create, name='log_new'),
    path('edit/<int:pk>', views.log_update, name='log_update'),
    path('delete/<int:pk>', views.log_delete, name='log_delete'),
]