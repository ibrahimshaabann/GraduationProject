from django.contrib import admin
from django.urls import path

from app.views.user import CreateUser, DestroyUser, LoginUserView, RetrieveUser, UpdateUser
from app.views.post import CommentPost, CreatePost, DestroyPost, FollowUser, RetrievePost, RetrieveUserPosts, UpdatePost, LikePost, GetAllPosts , ListNotifications , HandleNotification

urlpatterns = [
    path('user/create/', CreateUser.as_view()),
    path('user/login/', LoginUserView.as_view()),
    path('user/<int:pk>/', RetrieveUser.as_view()),
    path('user/update/', UpdateUser.as_view()),
    path('user/delete/<int:pk>', DestroyUser.as_view()),

    path('posts/', RetrieveUserPosts.as_view()),
    path('posts/all/', GetAllPosts.as_view()),
    path('post/create/', CreatePost.as_view()),
    path('post/<int:pk>/', RetrievePost.as_view()),
    path('post/update/<int:pk>/', UpdatePost.as_view()),
    path('post/delete/<int:pk>/', DestroyPost.as_view()),
  
    path('post/like/<int:pk>/', LikePost.as_view()),
    path('notifications/', ListNotifications.as_view(), name='list-notifications'),
    path('notifications/<int:pk>/', HandleNotification.as_view(), name='handle-notification'),

    path('post/comment/<int:pk>/', CommentPost.as_view()),
    path('post/comments/<int:pk>/', CommentPost.as_view()),


    path('user/follow/<int:pk>/', FollowUser.as_view()),
]

