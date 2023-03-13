
"""debugging_cake_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cake_user.urls', namespace="cake_user")),
    path('', include('user_profile.urls', namespace="user_profile")),
    path('', include('posts.urls')),
    path('notifications/', include('notifications.urls')),
    path('', include('tag.urls', namespace="tag")),
    path('', include('chats.urls')),
    path('', include('dashboard.urls', namespace='index')),
    path('', RedirectView.as_view(url='/home/', permanent=True))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
