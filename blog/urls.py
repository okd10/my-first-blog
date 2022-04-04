from django.urls import path
from . import views

#このurlパターンは''(http:--8000/)にアクセスしたときにview--listに向かわせるためのもの
#nameはurlに名前をつけただけ（あとでいじりやすいように）

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
