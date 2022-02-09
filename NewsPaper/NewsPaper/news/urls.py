from django.urls import path
from .views import PostView, CategoryPostView, PostDetail, PostSearch, NewsAddView, NewsUpdateView, NewsDeleteView, AuthorDetail, ProfileUpdateView
from .views import make_author, subscribe_me

urlpatterns = [
    path('', PostView.as_view()),
    path('category/<int:pk>', CategoryPostView.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='news_detail'),
    path('newssearch/', PostSearch.as_view(), name='news_search'),
    path('add/', NewsAddView.as_view(), name='news_add'),
    path('<int:pk>/edit', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('profile/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('profile/<int:pk>/edit', ProfileUpdateView.as_view(), name='profile_update'),
    path('make_author/', make_author, name = 'make_author'),
    path('subscribe_me/<int:pk>/', subscribe_me, name='subscribe_me'),
]
