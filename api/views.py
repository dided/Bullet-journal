from rest_framework import renderers, viewsets, permissions
from rest_framework.decorators import action 
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly, OwnerOnly, ReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    permission_classes = (OwnerOnly,)


class BulletViewSet(viewsets.ModelViewSet):
    queryset = Bullet.objects.all() 
    serializer_class = BulletSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    permission_classes = (OwnerOnly,)

    def get_queryset(self):
        queryset = Bullet.objects.filter(user=self.request.user) 

        page = self.request.QUERY_PARAMS.get('page', None)
        
        if page is not None:
            if Page.objects.filter(page_number=page, user=self.request.user).exists():
                pageObj= Page.objects.filter(page_number=page, user=self.request.user)
                queryset = Bullet.objects.filter(page=pageObj[0].id) 
        
        return queryset

    def pre_save(self, obj):
        obj.user = self.request.user


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (OwnerOnly,)


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (OwnerOnly,) 

    def get_queryset(self):
        queryset = Page.objects.filter(user=self.request.user)

        user = self.request.user

        page_number = self.request.QUERY_PARAMS.get('page_number', None)
        
        if page_number is not None:

            queryset = queryset.filter(page_number=page_number, user=user)

        return queryset

    def pre_save(self, obj):
        if self.request.method == 'POST':
            if Page.objects.filter(user=self.request.user).order_by('-page_number').exists():
                last_obj = Page.objects.filter(user=self.request.user).order_by('-page_number')[0]
                obj.page_number = last_obj.page_number + 1 
            else:
                obj.page_number = 1
        obj.user = self.request.user


class PageCount(APIView):

    def get(self, request, format=None):
        page_count = Page.objects.filter(user=request.user).count()
        content = {'page_count': page_count}
        return Response(content)



class SignifierViewSet(viewsets.ModelViewSet):
    queryset = Signifier.objects.all()
    serializer_class = SignifierSerializer
    permission_classes = (ReadOnly,)

class BulletSignifierViewSet(viewsets.ModelViewSet):
    queryset = BulletSignifier.objects.all()
    serializer_class = BulletSignifierSerializer
    permission_classes = (ReadOnly,)



