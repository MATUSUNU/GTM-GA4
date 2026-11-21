from django.urls import path

from .views import index, ContactView, SuccessView

urlpatterns = [
    path("", index, name="index"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
]
