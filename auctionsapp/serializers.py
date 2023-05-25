from rest_framework import serializers
from .models import auction_topic , test

class Auction_Topic_Serializer(serializers.ModelSerializer):
    class Meta:
        model = auction_topic
        fields = ('__all__')
class Test2_Serializer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields = ('__all__')
