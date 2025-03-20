from django.urls import path
from cp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_post, name='create_post'),
    path('search/', views.search_posts, name='search'),
] 