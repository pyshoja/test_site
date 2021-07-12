from django.contrib import admin

# Register your models here.

from .models import My , Slider , Category , Post , support


# admin.site.register(Apiadress )


class supportadmin (admin.ModelAdmin):
    list_display = ('author','title_suppurt','name_user','phone_user','email_user')
admin.site.register(support , supportadmin)


class postadmin (admin.ModelAdmin):
    list_display = ('id','title','parent','author','date','preview','status')
admin.site.register(Post , postadmin)


class Categoryadmin (admin.ModelAdmin):
    list_display = ('id','title','parent','status')
admin.site.register(Category , Categoryadmin)



class myadmin (admin.ModelAdmin):
    list_display = ('id','name_site','name_admin','time_start','title')

admin.site.register(My , myadmin)

class slideradmin (admin.ModelAdmin):
    list_display = ('id','title')
admin.site.register(Slider , slideradmin)

