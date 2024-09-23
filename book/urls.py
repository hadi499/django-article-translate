from django.urls import path
from .views import *
urlpatterns = [ 
    path('', book_list, name='book_list'), 
    path('<int:book_id>/', book_detail, name='book_detail'), 
]
