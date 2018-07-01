from django.urls import path
from .views import TopPage


urlpatterns = [
    path("", TopPage.as_view()),
]
