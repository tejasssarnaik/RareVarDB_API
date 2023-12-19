from rest_framework import serializers, viewsets
from .models import Exceldata

class ExceldataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exceldata
        fields = '__all__'

class ExceldataViewset(viewsets.ModelViewSet):
    queryset = Exceldata.objects.all()
    serializer_class = ExceldataSerializer
