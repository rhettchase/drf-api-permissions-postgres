from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Brew
from .serializers import BrewSerializer

class BrewList(ListCreateAPIView):
    # Anything that inherits from ListAPI View is going to need 2 brews.
    # What is the collection of brews, aka the queryset
    # associate collection of brews and the serial number
    queryset = Brew.objects.all()

    #serializing
    serializer_class = BrewSerializer

class BrewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Brew.objects.all()
    serializer_class = BrewSerializer
