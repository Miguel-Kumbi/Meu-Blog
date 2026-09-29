from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<slug:slug>/edit', views.post_update, name='post_update'),
    path('post/<slug:slug>/delete', views.post_delete, name='post_delete'),
    path('post/<slug:slug>/publish/', views.post_publish, name='post_publish'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail')
]
