from django.contrib import admin
from django.urls import path, include
from sisApp import urls
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

