from django.urls import path
from . import views
urlpatterns = [
    path('list/',views.user_list),
    path('register/',views.register),
    path('login/',views.user_view),
    path('detail/<int:id>/',views.users),
    path('change_password/<int:id>/',views.change_password)
]