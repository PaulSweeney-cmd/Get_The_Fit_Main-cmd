from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('shopping_bag/', include('shopping_bag.urls')),
    path('store_checkout/', include('store_checkout.urls')),
    path('user_profile/', include('user_profile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
