
#serializer란 models 객체와 querysets 같은 복잡한 데이터를 JSON, XML과 같은 native 데이터로 바꿔주는 역할을 한다. 아래에서는 HyperlinkedModelSerializer라는 serializer를 사용한다.

from .models import Alert
from rest_framework import serializers


class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = ('server', 'message','time','ipAddress')

