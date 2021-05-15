
from django.urls import include, path
from rest_framework import routers
from core1.views import SocietyViewSet,BuildingViewSet,FlatViewset
from .views import *

router = routers.DefaultRouter()
router.register(r'buildings',BuildingViewSet)
router.register(r'flats',FlatViewset)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('societies',societyView.as_view()),
    path('', include(router.urls)),
    
]