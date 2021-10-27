from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from apps.info.models import FestivalTeam
from apps.info.serializers import FestivalTeamsSerializer


class FestivalTeamsViewSet(ListAPIView):
    queryset = FestivalTeam.objects.all()
    serializer_class = FestivalTeamsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("team",)
    pagination_class = None
