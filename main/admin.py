from django.contrib import admin

from main.models import Client, Mailing, MailingLog
from users.models import User

# Register your models here.
admin.site.register(Client)
admin.site.register(Mailing)
admin.site.register(MailingLog)
admin.site.register(User)
