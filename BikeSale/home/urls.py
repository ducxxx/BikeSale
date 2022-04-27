from django.urls import path
from . import views

urlpatterns = [
    path('create-bike/', views.create_bike),
    path('update-bike/<int:id>', views.update_bike),
    path('', views.get_bike),
    path('delete-bike/<int:id>', views.delete_bike)
]