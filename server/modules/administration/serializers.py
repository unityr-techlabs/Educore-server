from rest_framework import serializers
from . import models

class AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'