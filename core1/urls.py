
from django.urls import include, path
from rest_framework import routers
from core1.views import SocietyViewSet,BuildingViewSet,FlatViewset

router = routers.DefaultRouter()
router.register(r'societies', SocietyViewSet)
router.register(r'buildings',BuildingViewSet)
router.register(r'flats',FlatViewset)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]