from rest_framework.decorators import api_view
from rest_framework.response import Response

from cride.circles.models import Circle
from cride.circles.serializers.circles1 import (
    CreateCircleSerializer,
    CircleSerializer
)
@api_view(['GET'])
def list_circles(self):
    circles = Circle.objects.all()
    data = []
    for circle in circles:
        data.append({
            'name': circle.name,
            'slug_name': circle.slug_name,
            'rides_taken': circle.rides_taken,
            'rides_offered': circle.rides_offered,
            'members_limit': circle.members_limit
        })
    return Response(data)

@api_view(['GET'])
def list_circles_serializers(self):
    circles = Circle.objects.all()
    serializer = CircleSerializer(circles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_circles_serializers(request):
    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    circle = serializer.save()
    return Response(CircleSerializer(circle))
