






# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class C2015D(models.Model):
    date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c2015d'


class C2015H(models.Model):
    date = models.DateField(blank=True, null=True)
    time = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c2015h'


class City(models.Model):
    city = models.CharField(max_length=30)
    date = models.CharField(max_length=20, blank=True, null=True)
    time = models.CharField(max_length=20, blank=True, null=True)
    aqi = models.CharField(db_column='AQI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.CharField(db_column='PM25_h', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.CharField(db_column='PM10_h', max_length=20, blank=True, null=True)  # Field name made lowercase.
    co_h = models.CharField(db_column='CO_h', max_length=20, blank=True, null=True)  # Field name made lowercase.
    no2_h = models.CharField(db_column='NO2_h', max_length=20, blank=True, null=True)  # Field name made lowercase.
    o3_h = models.CharField(db_column='O3_h', max_length=20, blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.CharField(db_column='O3_8h', max_length=20, blank=True, null=True)  # Field name made lowercase.
    so2_h = models.CharField(db_column='SO2_h', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class Cityzuobiao(models.Model):
    city = models.CharField(max_length=30, blank=True, null=True)
    cit = models.CharField(max_length=30, blank=True, null=True)
    lat = models.CharField(max_length=30, blank=True, null=True)
    lon = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cityzuobiao'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class S2014D(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2014d'


class S2014H(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2014h'


class S2015D(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2015d'


class S2015H(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2015h'


class S2016D(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2016d'


class S2016H(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2016h'


class S2017D(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2017d'


class S2017H(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2017h'


class S201807(models.Model):
    city = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.CharField(max_length=30, blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.CharField(db_column='AQI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    aqi_grade = models.CharField(db_column='AQI_grade', max_length=30, blank=True, null=True)  # Field name made lowercase.
    primary_pollutants = models.CharField(max_length=30, blank=True, null=True)
    pm25 = models.CharField(db_column='PM25', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pm10 = models.CharField(db_column='PM10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    co2 = models.CharField(db_column='CO2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    no2 = models.CharField(db_column='NO2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    o3_h = models.CharField(db_column='O3_h', max_length=20, blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.CharField(db_column='O3_8h', max_length=20, blank=True, null=True)  # Field name made lowercase.
    so2 = models.CharField(db_column='SO2', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's201807'


class S2018D(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2018d'


class S2018DCopy(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2018d_copy'


class S2018H(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2018h'


class S2018HCopy(models.Model):
    date = models.CharField(max_length=20, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's2018h_copy'


class Site(models.Model):
    city = models.CharField(max_length=30)
    date = models.CharField(max_length=30, blank=True, null=True)
    time = models.CharField(max_length=30, blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.CharField(db_column='AQI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    aqi_grade = models.CharField(db_column='AQI_grade', max_length=30, blank=True, null=True)  # Field name made lowercase.
    primary_pollutants = models.CharField(max_length=30, blank=True, null=True)
    pm25 = models.CharField(db_column='PM25', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pm10 = models.CharField(db_column='PM10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    co2 = models.CharField(db_column='CO2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    no2 = models.CharField(db_column='NO2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    o3_h = models.CharField(db_column='O3_h', max_length=20, blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.CharField(db_column='O3_8h', max_length=20, blank=True, null=True)  # Field name made lowercase.
    so2 = models.CharField(db_column='SO2', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'site'


class Sitezuobiao(models.Model):
    ids = models.CharField(max_length=30, blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    cit = models.CharField(max_length=30, blank=True, null=True)
    lon = models.CharField(max_length=30, blank=True, null=True)
    lat = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sitezuobiao'


class Tablename(models.Model):
    date = models.DateField(blank=True, null=True)
    site = models.CharField(max_length=30, blank=True, null=True)
    aqi = models.IntegerField(db_column='AQI', blank=True, null=True)  # Field name made lowercase.
    pm25_h = models.IntegerField(db_column='PM25_h', blank=True, null=True)  # Field name made lowercase.
    pm10_h = models.IntegerField(db_column='PM10_h', blank=True, null=True)  # Field name made lowercase.
    co_h = models.FloatField(db_column='CO_h', blank=True, null=True)  # Field name made lowercase.
    no2_h = models.IntegerField(db_column='NO2_h', blank=True, null=True)  # Field name made lowercase.
    o3_h = models.IntegerField(db_column='O3_h', blank=True, null=True)  # Field name made lowercase.
    o3_8h = models.IntegerField(db_column='O3_8h', blank=True, null=True)  # Field name made lowercase.
    so2_h = models.IntegerField(db_column='SO2_h', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tablename'
