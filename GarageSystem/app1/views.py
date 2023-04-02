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
def CreateFeedBack(request):
    data = request.data
    feed = FeedBack.objects.create(
        garage_id=Garage.objects.get(id=data['garage_id']),
        driver_id=User.objects.get(id=data['driver_id']),
        feed=data['feed'],
    )

    response = {'message': "success"}
    return Response(response)

# {
#     "garage_id": 1,
#     "driver_id": 2,
#     "feed": "good service",
# }


@api_view(['GET'])
@permission_classes([AllowAny])
def GarageFeeds(request, garage_id):
    garage = Garage.objects.get(id=garage_id)
    feeds = FeedBack.objects.values('id', 'driver_id', 'feed').filter(garage_id=garage)
    f = [e for e in feeds]
    feedback = []
    for d in f:
        user = User.objects.get(id=d['driver_id'])
        data = {
            'id': d['id'],
            'feed': d['feed'],
            'phone': user.phone,
            'email': user.email
        }
        feedback.append(data)
    return Response(feedback)


@api_view(['GET'])
@permission_classes([AllowAny])
def FeedInfo(request, feed_id):
    feed = FeedBack.objects.get(id=feed_id)
    user = User.objects.get(id=feed.driver_id)
    data = {
        'id': feed.id,
        'feed': feed.feed,
        'phone': user.phone,
        'email': user.email
    }
    return Response(data)

