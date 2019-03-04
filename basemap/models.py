# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Metadata(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metadata'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'sqlite_stat1'


class Tiles(models.Model):
    zoom_level = models.IntegerField(blank=True, null=True)
    tile_column = models.IntegerField(blank=True, null=True)
    tile_row = models.IntegerField(blank=True, null=True)
    tile_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tiles'
        unique_together = (('zoom_level', 'tile_column', 'tile_row'),)
