from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('biblioweb.account.urls')),
    path('books/', include('biblioweb.books.urls')),
    path('', include('biblioweb.main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
