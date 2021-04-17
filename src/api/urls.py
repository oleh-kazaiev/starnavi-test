from django.urls import path, include
from rest_framework import routers

from .auth import views as auth_views
from .post import views as post_views
from .analitics import views as analitics_views


router = routers.DefaultRouter()

urlpatterns = [
    path('sign-un/', auth_views.SignUpView.as_view()),
    path('sign-in/', auth_views.SignInView.as_view()),

    path('post/create/', post_views.PostCreateView.as_view()),
    path('post/like/<int:id>/', post_views.PostLikeView.as_view()),
    path('post/dislike/<int:id>/', post_views.PostDislikeView.as_view()),
    path('analitics/', analitics_views.AnaliticsView.as_view()),
    path('last-request/', analitics_views.LastRequestView.as_view()),

    path('', include(router.urls)),
]
