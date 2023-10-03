from rest_framework import serializers

from .models import Product, LikeProduct, MyProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'available', 'photo', 'short_description', 'price')


class MyProductSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=500)
    short_description = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=7, decimal_places=2)
    photo = serializers.ImageField()
    available = serializers.BooleanField(default=True)

    class Meta:
        model = MyProduct
        fields = ('user', 'name', 'description', 'available', 'photo', 'short_description', 'price')

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
