from django.urls import path
from .views import PostView, PostDetail

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]
