from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import certificationsSerializer
from .models import certifications


@api_view(['GET','POST'])
def certifications_list(request):
    if request.method == 'GET':
        data = certifications.objects.all()

        serializer = certificationsSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = certificationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def certification_detail(request, id):
    try:
        certificationDto = certifications.objects.get(id=id)
    except certifications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = certificationsSerializer(certificationDto, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        certificationDto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


