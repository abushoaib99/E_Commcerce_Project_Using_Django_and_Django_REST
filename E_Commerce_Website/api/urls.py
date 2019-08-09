from django.urls import path
from .views import ProductAPIView,CategoryAPIView, HistoryAPIView


urlpatterns = [
    path('', CategoryAPIView.as_view()),
    path('product/', ProductAPIView.as_view()),
    path('history/', HistoryAPIView.as_view()),
]
