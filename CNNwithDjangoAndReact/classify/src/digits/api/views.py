from digits.api.serializers import DigitSerializers
from rest_framework import viewsets
from ..models import Digit
from .serializers import DigitSerializers

class DigitViewSet(viewsets.ModelViewSet):
    serializer_class = DigitSerializers
    queryset = Digit.objects.all()


