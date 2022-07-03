import imp
from django.contrib import admin
from .models import Blog,Category,SubCategory,Contact,SubscriberEmail


class BlogsCategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['id','name']

class BlogsSubCategoryAdmin(admin.ModelAdmin):
    model = SubCategory
    list_display = ['id','name','mainCategory']


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ['id','title','category','likes','createdAt','author',"postStatus"]

class SubscriberEmailAdmin(admin.ModelAdmin):
    model = SubscriberEmail
    list_display = ['id','email',"subscriptionDate"]


class ContactModelAdmin(admin.ModelAdmin):
    list_display=('full_name','email','message','sent_date')


admin.site.register(Category,BlogsCategoryAdmin)
admin.site.register(SubCategory,BlogsSubCategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(SubscriberEmail,SubscriberEmailAdmin)
admin.site.register(Contact,ContactModelAdmin)
