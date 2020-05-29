from rest_framework import authentication
from users.models import Sefrtg
from .serializers import SefrtgSerializer
from rest_framework import viewsets


class SefrtgViewSet(viewsets.ModelViewSet):
    serializer_class = SefrtgSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Sefrtg.objects.all()
