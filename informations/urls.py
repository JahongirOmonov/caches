from django.urls import path

from informations.views import BookListApiView, UserMeRetrieveApiView

urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('user/<int:pk>/', UserMeRetrieveApiView.as_view()),
]
