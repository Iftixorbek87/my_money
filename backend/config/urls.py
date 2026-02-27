from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls')),
    path('', include('accounts.urls')),
    path('', include('transactions.urls')),
]

# Vercel uchun to'g'ri yo'naliklarimiz
if not settings.DEBUG:
    urlpatterns += [
        path('', include('accounts.urls')),
        path('', include('transactions.urls')),
    ]
