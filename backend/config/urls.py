from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('transactions.urls')),
]

# Vercel uchun root path ni qo'shimiz
if not settings.DEBUG:
    urlpatterns += [
        path('', include('accounts.urls')),
        path('', include('transactions.urls')),
    ]
