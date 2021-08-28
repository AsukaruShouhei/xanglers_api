from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Admin Login'

urlpatterns = [
    path('api/', include('posts.urls')),
    path('api/auth/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
