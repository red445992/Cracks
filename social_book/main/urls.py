from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('logout/',logout,name='logout'),
    path('settings/',settings,name="settings"),
    path('upload/',upload,name="upload"),
    path('like-post/<uuid:post_id>/', like_post, name='like-post'),
    path('profiles/<str:pk>', profiles, name='profiles')
]
