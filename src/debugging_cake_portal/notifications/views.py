from django.template import loader
from django.http import HttpResponse

from notifications.models import Notification


# Create your views here.

def show_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')
    Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)
    template = loader.get_template('notifications.html')
    context = {
        'notifications': notifications,
    }

    return HttpResponse(template.render(context, request))
