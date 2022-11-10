from django.contrib import admin
from django.urls import path, include
from draws import urls as draw_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("draws/",include(draw_urls))
]
