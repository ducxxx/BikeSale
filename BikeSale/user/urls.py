from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.create_user),
    path('get-user-info/<int:id>/', views.get_user, name='get_user'),
    path('update-user/<int:id>/', views.update_user),
    path('admin-get-user/', views.admin_get_user),
    path('create-admin/', views.create_admin),
    path('update-admin/<int:id>/', views.update_admin),
    path('admin-delete/<int:id>/', views.admin_delete, name='admin_delete')
]