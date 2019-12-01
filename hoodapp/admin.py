from django.contrib import admin
from .models import User, RegularProfile , AdminProfile

admin.site.register(User)
admin.site.register(RegularProfile)
admin.site.register(AdminProfile)

