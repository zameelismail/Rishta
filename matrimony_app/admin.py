from django.contrib import admin
from matrimony_app.models import Contact, Profile, Interest
from django.contrib.auth.models import Group, User

# Register your models here.

# admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Interest)
admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile
    
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "first_name", "last_name", "email"]
    inlines=[ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)