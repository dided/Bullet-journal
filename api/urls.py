from django.conf.urls import patterns, include, url
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'bullets', BulletViewSet)
router.register(r'signifiers', SignifierViewSet)
router.register(r'pages', PageViewSet)
router.register(r'bullet-signifier', BulletSignifierViewSet)
router.register(r'collections', CollectionViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'count', PageCount.as_view())
)
