
from django.urls import path,include
from .views import PostListView,PostdetailView
urlpatterns = [
    path('',PostListView.as_view(),name='post_list'),
    path('<int:pk>/',PostdetailView.as_view(),name='post_detail'),
]
