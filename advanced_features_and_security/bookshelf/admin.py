from django.contrib import admin
from .models import CustomUser, CustomUserManager


# Register your models here. =
from .models import Book 
class BookAdmin(admin.ModelAdmin):
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')
    list_display = ('title', 'author', 'publication_year')
admin.site.register(Book, BookAdmin)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_of_birth', 'profile_photo')
    

    