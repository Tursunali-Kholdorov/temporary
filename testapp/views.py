from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, generics, viewsets, filters

from .serializers import LicenseSerializer, CarSerializer, OrderCarSerializer
from .models import Car


class LicenseViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = LicenseSerializer
    permission_classes = []

    def get_queryset(self):
        return []


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'order')

    def get_serializer_class(self):
        if self.action == 'order':
            return OrderCarSerializer
        return CarSerializer

    @action(methods=['PUT'], detail=False)
    def order(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.save())
