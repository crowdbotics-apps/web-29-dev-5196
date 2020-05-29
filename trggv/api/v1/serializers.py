from rest_framework import serializers
from trggv.models import Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"
