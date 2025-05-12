from django.urls import path
from . import views

urlpatterns = [
    path("catalogo/", views.PetCatalogView.as_view(), name="pet_catalog"),
    path('create/', views.create_pet, name='create_pet'),
    path('pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('pet/<int:pet_id>/edit/', views.edit_pet, name='edit_pet'),
    path('pet/<int:pet_id>/delete/', views.delete_pet, name='delete_pet'),
    path('api/available-pets/', views.AvailablePetsListView.as_view(), name='available_pets_api'),
    
]