from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Blog,Contact,Category
from django.core.paginator import Paginator
from django.views import View
import random

def index(request):
    return render(request,'calculator/index.html')


class BlogCategoryView(View):
    def get(self,request,blogsCategory):
        cate = Category.objects.filter(slug=blogsCategory)
        blog = []
        myCategory = ""
        if cate.exists():
                blog = Blog.objects.filter(category=cate[0].id).filter(postStatus=True).order_by("-id")
                myCategory = cate[0].name

        paginator = Paginator(blog, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context={
            'blogs':page_obj,
            'category':myCategory
        }
        return render(request,"calculator/category-wise-blogs.html",context)

def AllBlogs(request):
    blog = Blog.objects.all().filter(postStatus=True).order_by('-id')
    paginator = Paginator(blog, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
    "blogs":page_obj
    }
    return render(request,'calculator/blogs.html',context)

class BlogDetail(View):
    def get(self,request,blogDetail):
        blog = Blog.objects.get(slug=blogDetail)
        # print(blog.tags.all())

        blogList=[]
        #in my blog detail  related posts
        # blogs = Blog.objects.all().filter(postStatus=True).filter(category=blog.category)
        #for now all as we donot have more data
        blogs = Blog.objects.all().filter(postStatus=True)
        for i in blogs:
            if len(blogList) < 4:
                i = random.randint(0,len(blogs))
                if Blog.objects.filter(id=i).exists():
                    blg = Blog.objects.get(id=i)
                    if not blg in blogList and not blg==blog:
                        blogList.append(blg)
        context={
            "blog":blog,
            "related":blogList,
        }
        return render(request,"calculator/blogDetails.html",context)

def aboutUs(request):
    return render(request,'calculator/about.html')


class contactUs(View):
    def get(self,request):
        return render(request,'calculator/contact.html')
    
    def post(self,request):
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        if full_name == '' or email == '' or message == '':
            messages.error(request,'Please fill all the fields')
            return redirect(request.META['HTTP_REFERER'])
        messages.success(request,'Message sent successfully')
        Contact.objects.create(full_name=full_name,email=email,message=message)
        return redirect('/')

def privacyPolicy(request):
    return render(request,'calculator/privacy.html')


def searchResults(request):
    blogs = Blog.objects.filter(title__icontains=request.GET['q'])
    context={
       "blogs":blogs,
        "total":len(blogs),
    }
    return render(request,"pages/search.html",context)