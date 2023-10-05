from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PostDetailView   

urlpatterns = [
    path("", views.IndexpageView.as_view(), name='index-view'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail-page'),
    path('tag/<slug:slug>/', views.tag_post_list, name='tag_post_list'),
    path('authors/<slug:author_slug>/posts/', views.author_posts, name='author_posts'),
    path("random-cheese-adventure/", views.random_page, name="random-page"),
    path("cheese/", views.cheese_page, name="cheese-page"),
    path("about_us/", views.cheese_manifesto, name="cheese-manifesto"),
     path('search/', views.search_view, name='search-view')
]
