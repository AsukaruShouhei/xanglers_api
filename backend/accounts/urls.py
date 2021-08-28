from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('obtain_token/', obtain_jwt_token, name='obtain_token'),
    path('refresh_token/', refresh_jwt_token, name='refresh_token'),
    path('verify_token/', verify_jwt_token, name='verify_token'),
]
