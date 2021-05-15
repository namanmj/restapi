
from django.urls import include, path
from rest_framework import routers
from .views import SocietyViewSet,BuildingViewSet
from .views import *
router = routers.DefaultRouter()
router.register(r'buildings',BuildingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('societies',societyView.as_view()),
    path('', include(router.urls))
]