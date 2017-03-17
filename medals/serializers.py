from django.contrib.auth.models import User, Group
from rest_framework import serializers
from medals.models import FullyUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class FullyUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    slackName = serializers.CharField(required=True, max_length=50)


    def create(self, validated_data):
        return FullyUser.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slackName = validated_data.get('slackName', instance.slackName)
        instance.save()

