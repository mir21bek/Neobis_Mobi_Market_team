from .models import LikeProduct
from django.db.models import Count


def get_like(user, product):
    like_record, created = LikeProduct.objects.get_or_create(user=user, product=product)
    if created:
        like_record.like = True
        like_record.save()
        return True
    else:
        return False


def delete_like(user, product):
    try:
        like_record = LikeProduct.objects.get(user=user, product=product)
        like_record.like = False
        like_record.save()
        return True
    except LikeProduct.DoesNotExist:
        return False


def get_like_count():
    likes_per_product = LikeProduct.objects.values('product').annotate(like_count=Count('product'))
    return likes_per_product
