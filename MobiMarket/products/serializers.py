from rest_framework import serializers

from .models import Product, LikeProduct, MyProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'available', 'photo', 'short_description', 'price')

    def create(self, validated_data):
        product = Product.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            available=validated_data['available'],
            photo=validated_data['photo'],
            short_description=validated_data['short_description'],
            price=validated_data['price'],
        )
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('descriptions', instance.description)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.available = validated_data.get('available', instance.available)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class LikeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeProduct
        fields = ('user', 'product', 'like')
