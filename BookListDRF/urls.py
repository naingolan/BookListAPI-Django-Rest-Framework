from django.urls import path, include
from .views import *

urlpatterns = [
    path('books', BookView.as_view()),
    path('books/<int:pk>', SingleBookView.as_view()),
]
