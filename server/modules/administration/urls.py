from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

admin_router = DefaultRouter()
admin_router.register(r'',views.AdministrationViewSet)

urlpatterns = [
    path('', include(admin_router.urls), name='admin'),
]