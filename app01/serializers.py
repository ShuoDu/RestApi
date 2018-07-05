# -*- coding:utf8 -*-
from rest_framework import serializers
from app01 import models

#
# # 自定义序列化
# class PublisherSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=32)
#     address = serializers.CharField(max_length=128)
#     def create(self, validated_data):
#         return models.Publisher.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.address = validated_data.get('address', instance.address)
#         instance.save()
#         return instance


class PublisherSerializer(serializers.ModelSerializer):
    operator = serializers.ReadOnlyField(source="operator.username")

    class Meta:
        model = models.Publisher   # model也是固定的
        fields = (
            "id",
            "name",
            "address",
            "operator",
        )


class BookSerializer(serializers.ModelSerializer):
    # publisher = serializers.ReadOnlyField(source="operator.username")

    class Meta:
        model = models.Books   # model也是固定的
        fields = (
            "id",
            "name",
            "publisher",
        )

