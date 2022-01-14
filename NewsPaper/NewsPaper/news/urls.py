from django.urls import path
from .views import PostView, PostDetail, PostSearch, NewsAddView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='news_detail'),
    path('newssearch/', PostSearch.as_view(), name='news_search'),
    path('add/', NewsAddView.as_view(), name='news_add'),
    path('<int:pk>/edit', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
]
