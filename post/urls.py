from django.urls import path
from . import views


app_name = 'post'

urlpatterns = [
    path('', views.post_list , name='post_list'),
    path('<int:id>', views.post_datail , name='post_datail'),
    path('<int:id>/edit', views.post_edit , name='post_edit'),
    path('create', views.post_create , name='post_create'),
]