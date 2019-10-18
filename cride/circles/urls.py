"""Circles URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import circles as circle_views
from .views import circlemetodo as circle_views2
from .views import memberships as membership_views

router = DefaultRouter()
router.register(r'circles', circle_views.CircleViewSet, basename='circle')
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-0_]+)/members',
    membership_views.MembershipViewSet,
    basename='membership'
)

urlpatterns = [
    path('circles/circle1', circle_views2.list_circles),
    path('circles/circle2', circle_views2.list_circles_serializers),
    path('circles/create', circle_views2.create_circles_serializers),
    path('', include(router.urls))
]
