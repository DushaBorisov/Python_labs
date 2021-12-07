from rest_framework import serializers

from simple_app.models import Houses, Streets


class HouseSerializer(serializers.ModelSerializer):
    class Meta:

        model = Houses
        fields = "__all__"


class StreetSerializer(serializers.ModelSerializer):
    class Meta:

        model = Streets
        fields = "__all__"
