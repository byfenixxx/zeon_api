from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("api/v1/auth/", include("rest_framework.urls")),
    path("api/v1/products/", ProductApiView.as_view()),
    path("api/v1/products/<int:pk>/", ProductApiView.as_view()),
    path("api/v1/products/<int:pk>/<str:slug>/", ProductApiView.as_view()),
    path("api/v1/collections/", CollectionApiView.as_view()),
    path("api/v1/news/", NewsApiView.as_view()),
    path("api/v1/help/", HelpApiView.as_view()),
    path("api/v1/aboutus/", AboutUsApiView.as_view()),
    path("api/v1/publicoffer/", PublicOfferApiView.as_view()),
    path("api/v1/newproducts/", NewProductsApiView.as_view()),
    path("api/v1/ourcontacts/", OurContactsApiView.as_view()),
    path("api/v1/sliders/", SliderApiView.as_view()),
    path("api/v1/ouradvantages/", OurAdvantagesApiView.as_view()),
    path("api/v1/footer/", FooterApiView.as_view()),
    path("api/v1/products/favourites/", FavouritesApiView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
