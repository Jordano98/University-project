from django.contrib import admin
from .models import University,City,Country

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=['name','city','type','address','created_date','published_date']


admin.site.register(University,PostAdmin)
admin.site.register(City)
admin.site.register(Country)