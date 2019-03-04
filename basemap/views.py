from django.shortcuts import render
from django.shortcuts import HttpResponse
from basemap import models  # 导入models文件

# Create your views here.


def index(request):
    return render(request, 'index.html')

def get_Tile(request,z,x,y):
    z = int(z)
    x = int(x)
    y = int(y)
    if request.method == 'GET':
        y0 = (1 << z) - 1 - y
        # y0 = y
        rsp = HttpResponse(content_type = "application/x-protobuf")
        ARe_tile = models.Tiles.objects.filter(zoom_level = z, tile_column = x, tile_row =y0 ).values_list('tile_data')
        if(ARe_tile.exists()):
            Re_tile = ARe_tile[0][0]
            rsp.write(Re_tile)
            rsp['Content-Encoding'] = 'gzip'
            return rsp
        else:
            return rsp

def get_polyTile(request, option, z, x, y):
    data_dic = {0:'guo',1:'shen',2:'shi',3:'xian'}
    cho_map = data_dic[int(option)]
    z = int(z)
    x = int(x)
    y = int(y)
    if request.method == 'GET':
        y0 = (1 << z) - 1 - y
        # y0 = y
        rsp = HttpResponse(content_type="application/x-protobuf")
        ARe_tile = models.Tiles.objects.using(cho_map).filter(zoom_level=z, tile_column=x, tile_row=y0).values_list('tile_data')
        if (ARe_tile.exists()):
            Re_tile = ARe_tile[0][0]
            rsp.write(Re_tile)
            rsp['Content-Encoding'] = 'gzip'
            return rsp
        else:
            return rsp