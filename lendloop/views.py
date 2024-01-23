from django.http import HttpResponse
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from lendloop.serializers import RegistrationSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes

@api_view(["POST"])
@permission_classes([])
@authentication_classes([])
def registration_view(request):
    registration_data = request.data

    serializer = RegistrationSerializer(data=registration_data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
