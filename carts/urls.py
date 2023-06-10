from django.urls import path,include
from . import views
urlpatterns = [
    path('carts/<int:id>/',views.carts,name='Cart')
]