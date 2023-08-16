from django.contrib import admin

from main.models import Client, Mailing, Message, MailingLogs

# Register your models here.
admin.site.register(Client)
admin.site.register(Mailing)
admin.site.register(Message)
admin.site.register(MailingLogs)
