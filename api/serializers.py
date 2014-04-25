from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class BulletSerializer(serializers.ModelSerializer):
    collection = serializers.HyperlinkedRelatedField('collection',
                                                    view_name='collection-detail',
                                                    required=False)
    signifiers = serializers.HyperlinkedRelatedField('signifiers',
                                                    view_name='signifier-detail',
                                                    many=True,
                                                    read_only=True)

    class Meta:
        model = Bullet
        fields = ('id', 'collection', 'user', 'page', 'type', 'name', 'desc', 'done',)
        read_only_fields = ('user',)


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'user', 'title', 'page_number',)
        read_only_fields = ('page_number', 'user',)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection


class SignifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signifier


class BulletSignifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletSignifier



    

