from django.contrib import admin
from category.models import Category

# register your models here. 
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug', 'description', 'category_img')
    
admin.site.register(Category, CategoryAdmin)