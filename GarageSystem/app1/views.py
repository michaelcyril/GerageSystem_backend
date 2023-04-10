from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializer import *
from AuthUser.models import User
from geopy import distance


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def RegisterGarage(request):
    data = request.data
    garage = Garage.objects.create(
        name=data['name'],
        description=data['description'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        user_id=User.objects.get(id=data['user_id'])
    )

    response = {'message': "success"}
    return Response(response)


# {
#     "name": "my garage",
#     "description": "some description",
#     "latitude": "1.00000",
#     "longitude": "2.0000",
#     "user_id": 1
# }


@api_view(['POST'])
@permission_classes([AllowAny])
def RegisterEngineer(request):
    data = request.data
    garage = Engineer.objects.create(
        username=data['username'],
        phone=data['phone'],
        description=data['description'],
        garage_id=Garage.objects.get(id=data['garage_id'])
    )

    response = {'message': "success"}
    return Response(response)


# {
#     "username": "my garage",
#     "phone": "0693331836",
#     "description": "mechanical fullstack",
#     "garage_id": 1
# }


@api_view(['GET'])
@permission_classes([AllowAny])
def GetNearByGarage(request, lat, lon):
    garages = Garage.objects.all()
    nearby_garages = []
    for garage in garages:
        garage_location = (garage.latitude, garage.longitude)
        user_location = (lat, lon)
        d = distance.distance(garage_location, user_location).miles
        if d < 10:  # Only include garages within 10 miles
            nearby_garages.append({
                'id': garage.id,
                'name': garage.name,
                'description': garage.description,
                'distance': d,
            })
    return Response(nearby_garages)


@api_view(['GET'])
@permission_classes([AllowAny])
def GarageInfo(request, garage_id):
    garage = Garage.objects.get(id=garage_id)
    user = User.objects.get(id=garage.user_id)
    data = {
        'id': garage.id,
        'name': garage.name,
        'description': garage.description,
        'phone': user.phone,
        'email': user.email
    }
    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def CreateFeedBackRequest(request):
    data = request.data
    feed = FeedBackRequest.objects.create(
        garage_id=Garage.objects.get(id=data['garage_id']),
        driver_id=User.objects.get(id=data['driver_id']),
        latitude=data['latitude'],
        longitude=data['longitude']
    )

    response = {'message': "success"}
    return Response(response)


# {
#     "garage_id": 1,
#     "driver_id": 2,
#     "latitude": "2.00000",
#     "longitude": "3.00000"
# }


@api_view(['POST'])
@permission_classes([AllowAny])
def CreateFeedBackAppointment(request):
    data = request.data
    feed = FeedBackAppointment.objects.create(
        garage_id=Garage.objects.get(id=data['garage_id']),
        driver_id=User.objects.get(id=data['driver_id']),
        date=data['date']
    )

    response = {'message': "success"}
    return Response(response)


# {
#     "garage_id": 1,
#     "driver_id": 2,
#     "date": "06-03-2023",
# }


@api_view(['GET'])
@permission_classes([AllowAny])
def GarageFeeds(request, garage_id):
    garage = Garage.objects.get(id=garage_id)
    feed_requests = FeedBackRequest.objects.values('id', 'driver_id', 'latitude', 'longitude', 'is_received').filter(garage_id=garage)
    fr = [e for e in feed_requests]
    feedback_request = []
    for d in fr:
        user = User.objects.get(id=d['driver_id'])
        data = {
            'feed_id': d['id'],
            'driver_id': d['driver_id'],
            'phone': user.phone,
            'email': user.email,
            'latitude': d['latitude'],
            'longitude': d['longitude'],
            'is_received': d['is_received']
        }
        feedback_request.append(data)

    feed_appointment = FeedBackAppointment.objects.values('id', 'driver_id', 'date', 'created_at', 'is_received').filter(garage_id=garage)
    fa = [e for e in feed_appointment]
    feedback_appointment = []
    for d in fa:
        user = User.objects.get(id=d['driver_id'])
        data = {
            'feed_id': d['id'],
            'driver_id': d['driver_id'],
            'phone': user.phone,
            'email': user.email,
            'appointment_date': d['date'],
            'created_at': d['created_at'],
            'is_received': d['is_received']
        }
        feedback_appointment.append(data)
    feedback_data = {'request': feedback_request, 'appointment': feedback_appointment}
    return Response(feedback_data)


@api_view(['GET'])
@permission_classes([AllowAny])
def FeedRequestInfo(request, feed_id):
    feed = FeedBackRequest.objects.get(id=feed_id)
    user = User.objects.get(id=feed.driver_id)
    data = {
        'feed_id': feed.id,
        'user_id': user.id,
        'phone': user.phone,
        'email': user.email,
        'latitude': feed.latitude,
        'longitude': feed.longitude,
        'is_received': feed.is_received,
    }
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def FeedAppointmentInfo(request, feed_id):
    feed = FeedBackAppointment.objects.get(id=feed_id)
    user = User.objects.get(id=feed.driver_id)
    data = {
        'feed_id': feed.id,
        'user_id': user.id,
        'phone': user.phone,
        'email': user.email,
        'appointment_date': feed.date,
        'created_at': feed.created_at,
        'is_received': feed.is_received,
    }
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def toYesAppointment(request, feed_id):
    feed = FeedBackAppointment.objects.get(id=feed_id)
    if feed.is_received == 'no':
        feed.is_received = 'yes'
        feed.save()
    return Response({'done': True})


@api_view(['GET'])
@permission_classes([AllowAny])
def toApprovedAppointment(request, feed_id):
    feed = FeedBackAppointment.objects.get(id=feed_id)
    if feed.is_received == 'yes':
        feed.is_received = 'approved'
        feed.save()
    return Response({'done': True})


@api_view(['GET'])
@permission_classes([AllowAny])
def toYesRequest(request, feed_id):
    feed = FeedBackRequest.objects.get(id=feed_id)
    if feed.is_received == 'no':
        feed.is_received = 'yes'
        feed.save()
    return Response({'done': True})


@api_view(['GET'])
@permission_classes([AllowAny])
def toApprovedRequest(request, feed_id):
    feed = FeedBackRequest.objects.get(id=feed_id)
    if feed.is_received == 'yes':
        feed.is_received = 'approved'
        feed.save()
    return Response({'done': True})
