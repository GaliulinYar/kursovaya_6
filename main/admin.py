from django.contrib import admin

from main.models import Client, Mailing, MailingLogs
from users.models import User

# Register your models here.
admin.site.register(Client)
admin.site.register(Mailing)
admin.site.register(MailingLogs)
admin.site.register(User)
