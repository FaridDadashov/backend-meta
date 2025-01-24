from django import template
from datetime import datetime
from zoneinfo import ZoneInfo


register = template.Library()


@register.filter
def format_last_seen(value):
    # By specifying timezone we make sure that it gives local date.
    today = datetime.now(tz=ZoneInfo('Asia/Baku'))
    if value.date() == today.date():
        return f"Bugün, { value.strftime('%H:%M')}"
    return value.strftime('%H:%M, %d %B')
