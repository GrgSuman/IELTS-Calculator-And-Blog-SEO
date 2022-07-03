from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(default="")
   
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(default="")
    mainCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(default="")
    featuredImage = models.ImageField(default="defaultBG.png",upload_to="uploads/images")
    keywords = models.CharField(max_length=400,default="")
    metaDesc = models.CharField(max_length=400,default="")
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name="category",null=True,blank=True)
    subCategory = models.ManyToManyField(SubCategory,blank=True)
    body  =    HTMLField(blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.PROTECT,related_name="author")
    createdAt = models.DateTimeField(null=True)
    updated = models.BooleanField(default=False)
    postStatus = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def get_absolute_url(self):
        return reverse('contact')

    def __str__(self):
        return self.full_name

class SubscriberEmail(models.Model):
    email = models.EmailField()
    subscriptionDate = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.email