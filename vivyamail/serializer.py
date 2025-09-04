from rest_framework import serializers
from .models import Mail

class MailSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    mail = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    mobile = serializers.CharField(max_length=12)
    place = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Mail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.mail=validated_data.get(instance.mail)
        instance.name=validated_data.get(instance.name)
        instance.save()
        return instance
