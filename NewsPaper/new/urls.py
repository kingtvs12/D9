from django.urls import path
from .views import PostsList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='posts_detail'),
    path('search/', PostSearch.as_view(), name='posts_search'),
    path('create/', PostCreate.as_view(), name='new_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='new_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='new_delete'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),

]
