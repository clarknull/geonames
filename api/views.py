from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.renderers import JSONRenderer
from . import serializers
from . import models


class GetChildren(ListAPIView):
    serializer_class = serializers.Location
    model = models.Location
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        try:
            return self.model.objects.get(code=self.kwargs.get('code')).get_children()
        except self.model.DoesNotExist:
            raise NotFound(detail="Unsupported Code")


class Details(RetrieveAPIView):
    serializer_class = serializers.Location
    lookup_field = 'code'
    renderer_classes = [JSONRenderer]
    queryset = models.Location.objects.all()
