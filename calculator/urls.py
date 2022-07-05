from django.urls import path
from . import views
from .models import Blog

# sitemaps===============
from django.contrib.sitemaps import GenericSitemap 
from django.contrib.sitemaps.views import sitemap
from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    # changefreq = 'daily'

    def items(self):
        return ['index', 'about-us','contact-us','privacy-policy']

    def location(self, item):
        return reverse(item)

blog_items = {
    'queryset': Blog.objects.all(),
    'date_field':'createdAt',
}


urlpatterns = [
   path('',views.index,name='index'),
   path('category/<slug:blogsCategory>',views.BlogCategoryView.as_view(),name='category'),
   path('blogs',views.AllBlogs,name='all-blogs'),
   path("<slug:blogDetail>",views.BlogDetail.as_view(),name="blog-details"),
   path("ieltscalc/about",views.aboutUs,name="about-us"),
   path("ieltscalc/contact",views.contactUs.as_view(),name="contact-us"),
   path("ieltscalc/privacy-policy",views.privacyPolicy,name="privacy-policy"),

   path('sitemap.xml/', sitemap, 
        {
        'sitemaps': {
            'blog': GenericSitemap(blog_items, priority=0.6,protocol = 'https',changefreq = "weekly"),
            'static' : StaticViewSitemap
            },
        
        },
        name='django.contrib.sitemaps.views.sitemap'),
]


