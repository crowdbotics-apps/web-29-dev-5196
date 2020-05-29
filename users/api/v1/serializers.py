from rest_framework import serializers
from users.models import Sefrtg


class SefrtgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sefrtg
        fields = "__all__"
