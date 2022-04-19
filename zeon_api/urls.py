from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from main.views import *


router = SimpleRouter()
router.register("carts", CartApiView)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny, ),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("api/v1/auth/", include("rest_framework.urls")),
    path("api/v1/", include(router.urls)),
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
    path("api/v1/products/favourites/", FavouritesApiView.as_view()),
    # path("api/v1/carts/", CartApiView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
