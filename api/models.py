from django.db import models

from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User


class Page(TimeStampedModel):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    page_number = models.IntegerField(max_length=50)

    def __unicode__(self):
        return self.title


class Signifier(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Collection(TimeStampedModel):
    user = models.ForeignKey(User)
    page = models.ForeignKey(Page, default='1')
    topic = models.CharField(max_length=50)

    def __unicode__(self):
        return self.topic


class Bullet(TimeStampedModel):
    user = models.ForeignKey(User)
    collection = models.ForeignKey(Collection, null=True)
    page = models.ForeignKey(Page, default='1') 
    signifiers = models.ManyToManyField(Signifier, through='BulletSignifier')

    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250, null=True)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name + ' / ' + self.type


class BulletSignifier(models.Model):
    bullet = models.ForeignKey(Bullet)
    signifier = models.ForeignKey(Signifier)


class BulletCollection(models.Model):
    bullet = models.ForeignKey(Bullet)
    collection = models.ForeignKey(Collection)

