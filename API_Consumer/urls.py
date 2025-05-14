from django.urls import path
from . import views

urlpatterns = [
    path('consume/', views.nft_detail_view, name='consume_api'),
    
]