from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from .models import ariza_E
from .serializers import arizaSerializer
from django.shortcuts import render, redirect, get_object_or_404


class arizaViewSet(viewsets.ModelViewSet):
    """
    Ariza CRUD
    """
    queryset = ariza_E.objects.all()
    serializer_class = arizaSerializer

    # def get_object(self, pk):
    #     return get_object_or_404(queryset, pk=pk)

    def list(self, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


    # def retrieve(self, request, pk=None):
    #     user = self.get_object(pk)
    #     serializer = self.serializer_class(user)
    #     return Response(serializer.data)

    # def update(self):
    #     pass
    #
    # def partial_update(self):
    #     pass
    #
    # def destroy(self):
    #     pass



class GetByPINFL(APIView):
    queryset = ariza_E.objects.all()
    serializer_class = arizaSerializer

    def get(self, request, *args, **kwargs):
        pinfl = request.query_params["pinfl"]
        data = self.queryset.get(pinfl=pinfl)
        serializer = self.serializer_class(data)

        return Response(serializer.data)

