
from django.urls import include, path
from rest_framework import routers
from .views import SocietyViewSet,BuildingViewSet

router = routers.DefaultRouter()
router.register(r'societies', SocietyViewSet)
router.register(r'buildings',BuildingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]