from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts_list'),
    path('categories/', views.CategoryListView.as_view(), name='category_main'),
]
