from django.urls import path
from . import views  #api_sentiment_pred

urlpatterns = [
    path('', views.home),
    path('user', views.user)
]