from django.urls import path
# from .views import RegisterUser,LoginView
from rest_framework_simplejwt import views as jwt_views
from .views import *
app_name = 'app1'

urlpatterns = [
    path('registerGarage', RegisterGarage),
    path('registerEngineer', RegisterEngineer),
    path('nearBy/<slug:lat>/<slug:lon>', GetNearByGarage),
    path('garageInfo/<int:garage_id>', GarageInfo),
    path('createFeed', CreateFeedBack),
    path('garageFeeds/<int:garage_id>', GarageFeeds),
    path('feedInfo/<int:feed_id>', FeedInfo),
]
