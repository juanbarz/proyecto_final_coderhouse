from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tblog_app.urls')),
    path('autores/', include('django.contrib.auth.urls')),
    path('autores/', include('autores_app.urls')),
]
