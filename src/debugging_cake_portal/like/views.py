from django.shortcuts import render
from like.models import Like


def listLike(request):
    likes = Like.objects.all
    data = {
        'likes': likes
    }
    return render(request, 'index.html', data)

