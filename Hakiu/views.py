from django.shortcuts import render
from rest_framework import viewsets
from .models import HaikuModel
from .serializers import HaikuSerialzer

# Create your views here.
from .permissions import IsOwnerOrReadOnly


class HaikuModelViewSet(viewsets.ModelViewSet):

    permission_classes = [IsOwnerOrReadOnly]
    queryset = HaikuModel.objects.all()
    serializer_class = HaikuSerialzer
