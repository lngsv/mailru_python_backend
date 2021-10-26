from django.urls import path

from users.views import user_details, user_list, create_user

urlpatterns = [
        path('user/', user_details, name='user_details'),
        path('list/', user_list, name='user_list'),
        path('new/', create_user, name='create_user'),
]
