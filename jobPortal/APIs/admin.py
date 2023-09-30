from django.contrib import admin

from .models import *
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(File, SimpleHistoryAdmin)
admin.site.register(Profile)
admin.site.register(CustomUser)
