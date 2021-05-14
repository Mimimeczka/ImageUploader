from django.contrib import admin
from .models import User, Image, Settings, AccountType

admin.site.register(User)
admin.site.register(Image)
admin.site.register(Settings)
admin.site.register(AccountType)
