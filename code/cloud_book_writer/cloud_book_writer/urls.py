from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('documents/', include('cloudbook_app.urls')),
]

