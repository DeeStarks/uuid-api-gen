from rest_framework import serializers
from . import models

class UUIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UUID
        fields = ('uuid', 'created_at')
