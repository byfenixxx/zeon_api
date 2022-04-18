from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class NewsApiListPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = "page_size"


class ProductApiView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        search = request.query_params.get("search")
        if search:
            products = Product.objects.filter(title__icontains=search)
            return Response(ProductSerializer(products, many=True).data)
        if not pk:
            products = Product.objects.all()
            return Response(ProductSerializer(products, many=True).data)
        product = Product.objects.get(pk=pk)
        slug = kwargs.get("slug")
        if slug == "similar":
            similar = Product.objects.filter(collection=product.collection.id)
            return Response(ProductSerializer(similar, many=True).data)
        return Response(ProductSerializer(product).data)


class CollectionApiListPagination(PageNumberPagination):
    page_size = 2


class CollectionApiView(APIView, CollectionApiListPagination):
    def get(self, request):
        collection = Collection.objects.all()
        result_page = self.paginate_queryset(collection, request, view=self)
        return self.get_paginated_response(CollectionSerializer(result_page, many=True).data)


class NewsApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsApiListPagination


class HelpApiView(generics.ListAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer


class AboutUsApiView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class PublicOfferApiView(generics.ListAPIView):
    queryset = PublicOffer.objects.all()
    serializer_class = PublicOfferSerializer


class NewProductsApiView(generics.ListAPIView):
    queryset = Product.objects.filter(is_new=True)[:5]
    serializer_class = ProductSerializer


class OurContactsApiView(generics.ListAPIView):
    queryset = OurContacts.objects.all()
    serializer_class = OurContactsSerializer


class SliderApiView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class OurAdvantagesApiView(generics.ListAPIView):
    queryset = OurAdvantages.objects.all()
    serializer_class = OurAdvantagesSerializer


class FooterApiView(generics.ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer


class FavouritesApiView(generics.ListAPIView):
    queryset = Product.objects.filter(is_favourites=True)
    serializer_class = ProductSerializer


class CartApiView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
