from django.contrib import admin
from .models import User, RegularProfile , AdminProfile, Business, Neighbourhood

admin.site.register(User)
admin.site.register(RegularProfile)
admin.site.register(AdminProfile)
admin.site.register(Business)
admin.site.register(Neighbourhood)

