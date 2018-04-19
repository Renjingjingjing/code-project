# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Goods(models.Model):
    id = models.IntegerField(primary_key=True)
    # ui = models.ForeignKey('User', db_column='ui', blank=True, null=True)
    ui = models.IntegerField(unique=True, blank=True)
    goods = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=255, blank=True)
    material = models.CharField(max_length=255, blank=True)
    desc = models.CharField(max_length=255, blank=True)
    prize = models.CharField(max_length=255, blank=True)
    telephone = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    is_available = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'


class User(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(unique=True, max_length=255, blank=True)
    passwd = models.CharField(max_length=255, blank=True)
    mobilephone = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

    def __unicode__(self):
        return self.name
