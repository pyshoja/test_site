from django.contrib import admin

# Register your models here.

from .models import My , Slider , Category , Post


class postadmin (admin.ModelAdmin):
    list_display = ('id','title','parent','author','date','status')
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

