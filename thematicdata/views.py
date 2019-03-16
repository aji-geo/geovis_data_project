from django.shortcuts import render
from django.shortcuts import HttpResponse
from thematicdata import models  # 导入models文件
from datetime import datetime, timedelta, date
from geojson import Feature, FeatureCollection, Point
import geojson
import pandas
import math

def getFeature(lon,lat,my_properties):
    my_point = Point((lon,lat))
    return Feature(geometry=my_point, properties=my_properties)


def ditu(request):

    df = pandas.read_csv(r'basemap/static/files/233.csv')
    now_time = datetime.now()
    now_date = now_time.strftime('%Y-%m-%d')
    now_hour = now_time+timedelta(hours=7)
    re_hour = now_hour.strftime('%H')+":00:00"
    if re_hour == '03:00:00':
        re_hour = '02:00:00'
    else:
        re_hour = now_hour.strftime('%H')+":00:00"
    resdata = []
    print(now_date,re_hour)
    RealtimeAQI = models.Site.objects.using('aqi').filter(date=now_date, time=re_hour).values('site',
                                                                                              'aqi',
                                                                                              'city',
                                                                                              'date',
                                                                                              'time',
                                                                                              'aqi_grade',
                                                                                              'primary_pollutants')#返回字典类型
    for line in RealtimeAQI:

        zb = df[df.city == line['city']]
        try:
            siteinfo = zb[zb.site == line['site']].iloc[0]
        except IndexError:
            continue
        con_city = {'lon':siteinfo['jindu'], 'lat':siteinfo['weidu'], 'city':siteinfo['cit']}

        if math.isnan(con_city['lon']) or \
                math.isnan(con_city['lat']) or \
                line['aqi'] == '':

            continue
        myproperties = {'city':con_city['city'],
                        'site':line['site'],
                        'AQI':line['aqi'],
                        'date':line['date'],
                        'time':line['time'],
                        'AQI_grade':line['aqi_grade'],
                        'primary_pollutants':line['primary_pollutants']}

        myFeature = getFeature(con_city['lon'],con_city['lat'],myproperties)
        resdata.append(myFeature)
        myFeatureCollection = FeatureCollection(resdata)

    dump = geojson.dumps(myFeatureCollection)
    return HttpResponse(dump)