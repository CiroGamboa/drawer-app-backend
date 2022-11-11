from django.urls import path
from .views import (
    DrawListApiView,
    DrawDetailApiView
)

urlpatterns = [
    path('api', DrawListApiView.as_view()),
    path('api/<int:draw_id>/', DrawDetailApiView.as_view()),
]