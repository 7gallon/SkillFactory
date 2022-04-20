from django.urls import path, include
from .views import PostView, PostDetail, PostSearch, AuthorDetail, PostAddView, ProfileUpdateView, PostDeleteView, \
                   PostUpdateView, MessageView, MsgView, msg_submit

urlpatterns = [
    path('', PostView.as_view(), name='post_view'),
    path('board/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('postsearch/', PostSearch.as_view(), name='post_search'),
    path('accounts/profile/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('board/add/', PostAddView.as_view(), name='post_add'),
    path('board/message/', MessageView.as_view(), name='msg_add'),
    path('board/message/<int:pk>/submit', msg_submit, name='msg_submit'),
    path('board/msglist/', MsgView.as_view(), name='msg_list'),
    path('board/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('board/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('accounts/profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_update'),

]
