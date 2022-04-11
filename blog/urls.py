from django.urls import path
from . import views

#この1つめのurlパターンは''(http:--8000/)にアクセスしたときにview--listに向かわせるためのもの
#nameはurlに名前をつけただけ（あとでいじりやすいように）

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
