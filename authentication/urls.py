from django.urls import path

from authentication.views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('registration', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
]
