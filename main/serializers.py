from rest_framework import serializers

from .models import *


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image", )


class ProductSerializer(serializers.ModelSerializer):
    collection = serializers.SlugRelatedField(slug_field="title", read_only=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "title", "articul", "price", "old_price",
            "description", "size", "material_composition",
            "collection", "images"
        )


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        exclude = ("id", )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ("id", )


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        exclude = ("id", )


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        exclude = ("id", )


class PublicOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicOffer
        exclude = ("id", )


class OurContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurContacts
        exclude = ("id", )


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        exclude = ("id", )


class OurAdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAdvantages
        exclude = ("id", )


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        exclude = ("id", )


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItems
        exclude = ("id", )


class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(many=True, write_only=True)

    def to_representation(self, instance):
        representation = super(CartSerializer, self).to_representation(instance)
        representation["products"] = CartItemSerializer(CartItems.objects.filter(cart=instance), many=True).data
        return representation

    class Meta:
        model = Cart
        exclude = ("id", )
