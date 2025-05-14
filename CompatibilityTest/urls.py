from django.urls import path
from . import views

urlpatterns = [
    path('test-compatibilidad/', views.compatibility_test, name='compatibility_test'),
]