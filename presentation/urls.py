from django.urls import path
from .presentation_views.presentation import Presentation
urlpatterns = [
    path("", Presentation.as_view(), name=""),
]
