from django.urls import path

from like.views import listLike

urlpatterns = [
    path('', listLike, name='show-likes')
]
