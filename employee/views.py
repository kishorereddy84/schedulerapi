from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import employeeSerializer, employeeAvailabiltySerializer
from .models import employee, employeeavailability


@api_view(['GET', 'POST'])
def employees_list(request):
    if request.method == 'GET':
        data = employee.objects.all()

        serializer = employeeSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            employeeavailabilityschedule(request.data, serializer.data)

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def employeeavailabilityschedule(employeedata, data):
    print('entered')
    schedule = employeedata['employeeAvailability']
    print(schedule)

    employeeid = data['id']
    employeeid = data['id']
    emp = employee.objects.get(id=employeeid)
    emp.employeeavailability_set.all().delete()
    timings = []

    for week in schedule:
        print(week)
        timing = employeeavailability(
            day=week['day'], availability=week['availability'], startTime=week['startTime'], endTime=week['endTime'], dayOfTheWeek=week['dayOfTheWeek'], employee=emp)
        timings.append(timing)

    employeeavailability.objects.bulk_create(timings)


@api_view(['PUT', 'DELETE'])
def employee_detail(request, id):
    try:
        employeeDto = employee.objects.get(id=id)
    except employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = employeeSerializer(
            employeeDto, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            employeeavailabilityschedule(request.data, serializer.data)

            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employeeDto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def default_employee_availability(request):
    employee_availability_schedule = [
        {
            "day": "sunday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "employee": 0,
            "dayOfTheWeek": 0
        },
        {
            "day": "monday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "employee": 0,
            "dayOfTheWeek": 1
        },
        {
            "day": "tuesday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "employee": 0,
            "dayOfTheWeek": 2
        },
        {
            "day": "wednesday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "employee": 0,
            "dayOfTheWeek": 3
        },
        {
            "day": "thursday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "employee": 0,
            "dayOfTheWeek": 4
        },
        {
            "day": "friday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "employee": 0,
            "dayOfTheWeek": 5
        },
        {
            "day": "saturday",
            "availability": 0,
            "startTime": "00:00:00",
            "endTime": "00:00:00",
            "employee": 0,
            "dayOfTheWeek": 6
        }
    ]
    return Response(employee_availability_schedule)


@api_view(['GET', 'POST'])
def employeeavailability_list(request, empid):

    if request.method == 'GET':
        try:
            emp = employee.objects.get(id=empid)
            data = emp.employeeavailability_set.all()
        except:
            raise 404

        serializer = employeeAvailabiltySerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        print(empid)
        timings = []
        emp = employee.objects.get(id=empid)
        data = emp.employeeavailability_set.all().delete()
        # departmenttimings.objects.get(department=dept).delete()
       # departmenttimings.objects.bulk_create(request.data)

        for week in request.data:
            print(week)
            timing = employeeavailability(
                day=week['day'], availability=week['availability'], startTime=week['startTime'], endTime=week['endTime'], dayOfTheWeek=week['dayOfTheWeek'], employee=employee.objects.get(id=empid))
            timings.append(timing)

        employeeavailability.objects.bulk_create(timings)
        serializer = employeeAvailabiltySerializer(data=request.data)
        # print(request.data)
        # print(serializer.is_valid)
        # # {"weekday":"sunday","startTime":"09:00","endTime":"05:00","department":"1"}
        # if serializer.is_valid():
        #     print("entered")
        #     serializer.save()
        #     return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
