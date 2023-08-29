from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('scheduling/', include('scheduling.urls')),
    path('', include('landing.urls')),
    path('admin/', admin.site.urls),
]
