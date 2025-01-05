from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'Email', 'phone']
    search_fields = ['username', 'phone']


admin.site.register(User, UserAdmin)

# Register your models here.
