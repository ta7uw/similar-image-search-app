from django.urls import path
from .views import TopPage
from settings import settings


urlpatterns = [
    path("", TopPage.as_view()),
    # TODO: media file path
    path("media/", "django.views.static.serve", {"docoument_root": settings.MEDIA_ROOT})
]
