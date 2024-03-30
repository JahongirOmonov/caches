from rest_framework import generics
from informations.models import Book
from informations.serializers import BookSerializer, UserSerializer
# from django.views.decorators.cache import cache_page
# from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from users.models import User
from rest_framework import status
from django.http import HttpResponse


class BookListApiView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        key = 'key_of_book'
        info_of_cached = cache.get(key)

        if info_of_cached is None:
            queryset = Book.objects.all()
            info_of_cached = list(queryset.values())
            print()
            print(info_of_cached)
            print()
            cache.set(key, info_of_cached, timeout=60*12)
        return info_of_cached


class UserMeRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        user_id = self.kwargs.get('pk')

        key = f'user_{user_id}'

        cached_data = cache.get(key)

        if cached_data is None:
            try:
                user_instance = User.objects.get(id=user_id)
                serializer = self.get_serializer(user_instance)
                cached_data = serializer.data

                cache.set(key, cached_data, timeout=60 * 13)
            except User.DoesNotExist:
                return HttpResponse("You entered wrong ID")

        return cached_data
