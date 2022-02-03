from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers

def list_to_dict(data: list) -> dict:
    return {row['created_at']: row['uuid'] for row in data}

@api_view(['GET'])
def uuid(request):
    uuidObj = models.UUID.objects
    uuidObj.create()
    uuidSer = serializers.UUIDSerializer(uuidObj, many=True)
    data = list_to_dict(data=uuidSer.data)
    return Response(data, status=200)