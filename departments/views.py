
from django.http import HttpResponse, Http404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from .serializers import departmentSerializer, departmenttimingsSerializer
from .models import department, departmenttimings


@api_view(['GET', 'POST'])
def department_list(request):
    if request.method == 'GET':
        data = department.objects.all()

        serializer = departmentSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = departmentSerializer(data=request.data)
        if serializer.is_valid():
            print("serialized data")
            serializer.save()
            print(serializer.data)
            departmentschedule(request.data, serializer.data)
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def departmentschedule(departmentData, data):
    print('entered')
    schedule = departmentData['departmentSchedules']
    print(schedule)

    departmentid = data['id']
    depart = department.objects.get(id=departmentid)
    depart.departmenttimings_set.all().delete()
    timings = []

    for week in schedule:
        print(week)
        timing = departmenttimings(
            day=week['day'], availability=week['availability'], startTime=week['startTime'], endTime=week['endTime'], dayOfTheWeek=week['dayOfTheWeek'], department=depart)
        timings.append(timing)

    departmenttimings.objects.bulk_create(timings)


@api_view(['PUT', 'DELETE'])
def department_detail(request, id):
    try:
        departmentDto = department.objects.get(id=id)
    except department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = departmentSerializer(
            departmentDto, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            departmentschedule(request.data, serializer.data)

            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        departmentDto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def default_department_schedule(request):
    department_default_schedule = [
        {
            "day": "sunday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "department": 0,
            "dayOfTheWeek": 0
        },
        {
            "day": "monday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "department": 0,
            "dayOfTheWeek": 1
        },
        {
            "day": "tuesday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "department": 0,
            "dayOfTheWeek": 2
        },
        {
            "day": "wednesday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "department": 0,
            "dayOfTheWeek": 3
        },
        {
            "day": "thursday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "department": 0,
            "dayOfTheWeek": 4
        },
        {
            "day": "friday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "department": 0,
            "dayOfTheWeek": 5
        },
        {
            "day": "saturday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "department": 0,
            "dayOfTheWeek": 6
        }
    ]
    return Response(department_default_schedule)


@api_view(['GET', 'POST'])
def departmenttimings_list(request, dept):

    if request.method == 'GET':
        try:
            depart = department.objects.get(id=dept)
            data = depart.departmenttimings_set.all()
        except:
            raise 404

        serializer = departmenttimingsSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        print(dept)
        timings = []
        depart = department.objects.get(id=dept)
        data = depart.departmenttimings_set.all().delete()
        # departmenttimings.objects.get(department=dept).delete()
       # departmenttimings.objects.bulk_create(request.data)

        for week in request.data:
            print(week)
            timing = departmenttimings(
                day=week['day'], availability=week['availability'], startTime=week['startTime'], endTime=week['endTime'], dayOfTheWeek=week['dayOfTheWeek'], department=department.objects.get(id=dept))
            timings.append(timing)

        departmenttimings.objects.bulk_create(timings)
        serializer = departmenttimingsSerializer(data=request.data)
        # print(request.data)
        # print(serializer.is_valid)
        # # {"weekday":"sunday","startTime":"09:00","endTime":"05:00","department":"1"}
        # if serializer.is_valid():
        #     print("entered")
        #     serializer.save()
        #     return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
