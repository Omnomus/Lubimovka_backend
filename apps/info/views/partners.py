from rest_framework.generics import ListAPIView

from apps.info.models import Partner
from apps.info.serializers import PartnerSerializer


class PartnersViewSet(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    filterset_fields = ("type",)
    pagination_class = None
