from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import Post

admin.site.register(Post)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)