from rest_framework.views import APIView
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from ... import models
from ... import serializers

class AdministrationViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.AdministrationSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['user_type','email','username']

    def get_queryset(self):
        queryset = super().get_queryset()
        role = self.request.query_params.get('user_type')
        if role:
            queryset = queryset.filter(role=role)
        return queryset
    
    def perform_create(self, serializer):
        admin = self.request.user
        if admin.user_type != 'admin':
            raise PermissionDenied("You are not allowed to create a user")
        
        serializer.save(created_by=self.request.user)

    
