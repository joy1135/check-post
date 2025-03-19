from django.urls import path
from cp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:post_id>/', views.post)
] 