
from django.http import HttpResponse, Http404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from .serializers import locationSerializer, locationtimingsSerializer
from .models import location, locationtimings


@api_view(['GET', 'POST'])
def location_list(request):
    if request.method == 'GET':
        data = location.objects.all()

        serializer = locationSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = locationSerializer(data=request.data)
        if serializer.is_valid():
            print("serialized data")
            serializer.save()
            print(serializer.data)
            locationschedule(request.data, serializer.data)
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def locationschedule(locationData, data):
    print('entered')
    schedule = locationData['locationSchedules']
    print(schedule)

    locationid = data['id']
    depart = location.objects.get(id=locationid)
    depart.locationtimings_set.all().delete()
    timings = []

    for week in schedule:
        print(week)
        timing = locationtimings(
            day=week['day'], availability=week['availability'], startTime=week['startTime'], endTime=week['endTime'], dayOfTheWeek=week['dayOfTheWeek'], location=depart)
        timings.append(timing)

    locationtimings.objects.bulk_create(timings)


@api_view(['PUT', 'DELETE'])
def location_detail(request, id):
    try:
        locationDto = location.objects.get(id=id)
    except location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = locationSerializer(
            locationDto, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            locationschedule(request.data, serializer.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        locationDto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def default_location_schedule(request):
    location_default_schedule = [
        {
            "day": "sunday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "location": 0,
            "dayOfTheWeek": 0
        },
        {
            "day": "monday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "location": 0,
            "dayOfTheWeek": 1
        },
        {
            "day": "tuesday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "location": 0,
            "dayOfTheWeek": 2
        },
        {
            "day": "wednesday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "location": 0,
            "dayOfTheWeek": 3
        },
        {
            "day": "thursday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "location": 0,
            "dayOfTheWeek": 4
        },
        {
            "day": "friday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "location": 0,
            "dayOfTheWeek": 5
        },
        {
            "day": "saturday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "location": 0,
            "dayOfTheWeek": 6
        }
    ]
    return Response(location_default_schedule)


@api_view(['GET', 'POST'])
def locationtimings_list(request, dept):

    if request.method == 'GET':
        try:
            depart = location.objects.get(id=dept)
            data = depart.locationtimings_set.all()
        except:
            raise 404

        serializer = locationtimingsSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        print(dept)
        timings = []
        depart = location.objects.get(id=dept)
        data = depart.locationtimings_set.all().delete()
        # locationtimings.objects.get(location=dept).delete()
       # locationtimings.objects.bulk_create(request.data)

        for week in request.data:
            print(week)
            timing = locationtimings(
                day=week['day'], availability=week['availability'], startTime=week['startTime'], endTime=week['endTime'], dayOfTheWeek=week['dayOfTheWeek'], location=location.objects.get(id=dept))
            timings.append(timing)

        locationtimings.objects.bulk_create(timings)
        serializer = locationtimingsSerializer(data=request.data)
        # print(request.data)
        # print(serializer.is_valid)
        # # {"weekday":"sunday","startTime":"09:00","endTime":"05:00","location":"1"}
        # if serializer.is_valid():
        #     print("entered")
        #     serializer.save()
        #     return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
