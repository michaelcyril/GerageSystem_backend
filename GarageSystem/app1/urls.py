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
    path('createFeedRequest', CreateFeedBackRequest),
    path('createFeedAppointment', CreateFeedBackAppointment),
    path('garageFeeds/<int:garage_id>', GarageFeeds),
    path('feedRequestInfo/<int:feed_id>', FeedRequestInfo),
    path('feedAppointmentInfo/<int:feed_id>', FeedAppointmentInfo),
    path('toYesRequest/<int:feed_id>', toYesRequest),
    path('toApprovedRequest/<int:feed_id>', toApprovedRequest),
    path('toYesAppointment/<int:feed_id>', toYesAppointment),
    path('toApprovedAppointment/<int:feed_id>', toApprovedAppointment),

]
