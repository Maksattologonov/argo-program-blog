from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/accounts/', include('authemail.urls')),
    path('admin/', admin.site.urls),
    path('courses/', include('course.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
