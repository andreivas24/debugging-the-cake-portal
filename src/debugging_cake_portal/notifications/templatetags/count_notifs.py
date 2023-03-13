from django import template

from notifications.models import Notification

register = template.Library()

@register.simple_tag
def count_notifications(request):
    count_notifications = Notification.objects.filter(user=request.user, is_seen=False).count()
    return count_notifications
