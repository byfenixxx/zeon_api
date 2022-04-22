from rest_framework import serializers

from .models import *


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image", )


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        exclude = ("id", )


class ProductSerializer(serializers.ModelSerializer):
    collection = serializers.SlugRelatedField(slug_field="title", read_only=True)
    images = ProductImageSerializer(many=True)
    colors = ColorSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "title", "articul", "price", "old_price",
            "description", "size", "material_composition",
            "collection", "images", "colors"
        )


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"


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


class CartItemsSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)

    def to_representation(self, instance):
        representation = super(CartItemsSerializer, self).to_representation(instance)
        representation["title"] = instance.product.title
        representation["images"] = ProductImageSerializer(instance.product.images, many=True).data
        representation["size"] = instance.product.size
        representation["color"] = ColorSerializer(instance.product.colors, many=True).data
        return representation

    class Meta:
        model = CartItems
        exclude = ("id", "cart")


class CartSerializer(serializers.ModelSerializer):
    products = CartItemsSerializer(many=True, write_only=True)
    total_sum = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)
    discount = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)
    final_total_sum = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    def create(self, validated_data):
        total_sum = 0
        discount = 0
        print(validated_data)
        products = validated_data.pop("products")
        cart = Cart.objects.create(**validated_data)
        for prod in products:
            total_sum += prod["product"].old_price * prod["quantity"]
            discount += (prod["product"].old_price - prod["product"].price) * 2
            CartItems.objects.create(cart=cart, **prod)
        cart.total_sum = total_sum
        cart.discount = discount
        cart.final_total_sum = total_sum - discount
        cart.save()
        return cart

    def to_representation(self, instance):
        representation = super(CartSerializer, self).to_representation(instance)
        representation["products"] = CartItemsSerializer(CartItems.objects.filter(cart=instance), many=True).data
        return representation

    class Meta:
        model = Cart
        exclude = ("id", )
