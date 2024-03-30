from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Book
from users.models import User


@receiver([post_save, post_delete], sender=Book)
def invalidate_book_cache(sender, instance, **kwargs):
    cache_key = 'key_of_book'
    cache.delete(cache_key)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>")


@receiver([post_save, post_delete], sender=User)
def invalidate_user_cache(sender, instance, **kwargs):
    cache_key = f'user_{instance.id}'

    cache.delete(cache_key)
