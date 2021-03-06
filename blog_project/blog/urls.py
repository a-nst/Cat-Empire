from django.urls import path 
from blog_project import settings
from .views import BlogListView, BlogDetailView, BLogCreateView, BlogUpdateView, BlogDeleteView, AboutView


urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit' ),
    path('post/new/', BLogCreateView.as_view(), name ='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name ='post_detail'),
    path('', BlogListView.as_view(), name ='home'),
    path('about/', AboutView.as_view(), name = 'about' )
]