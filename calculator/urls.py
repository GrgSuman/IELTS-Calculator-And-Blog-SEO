from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('category/<slug:blogsCategory>',views.BlogCategoryView.as_view(),name='category'),
   path('blogs',views.AllBlogs,name='all-blogs'),
   path("<slug:blogDetail>",views.BlogDetail.as_view(),name="blog-details"),
   path("ieltscalc/about",views.aboutUs,name="about-us"),
   path("ieltscalc/contact",views.contactUs.as_view(),name="contact-us"),
   path("ieltscalc/privacy-policy",views.privacyPolicy,name="privacy-policy"),
]
