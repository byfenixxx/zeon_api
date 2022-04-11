from django.contrib import admin
from django.urls import path, include
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("api/v1/products/", ProductApiView.as_view()),
    path("api/v1/products/<int:pk>/", ProductApiView.as_view()),
    path("api/v1/products/<int:pk>/<str:slug>/", ProductApiView.as_view()),
    path("api/v1/collections/", CollectionApiView.as_view()),
    path("api/v1/news/", NewsApiView.as_view()),
    path("api/v1/help/", HelpApiView.as_view()),
    path("api/v1/aboutus/", AboutUsApiView.as_view()),
    path("api/v1/publicoffer/", PublicOfferApiView.as_view()),
    path("api/v1/newproducts/", NewProductsApiView.as_view()),
    path("api/v1/ourcontacts/", OurContactsApiView.as_view())
]
