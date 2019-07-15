# -*- coding: utf-8 -*-
from osgeo import gdal
from osgeo import ogr

# shpFile = "F:/arcgis/temp/hpu/学院楼.shp"
shpFile = "./data/roads_2.shp"
# 0表示只读，1表示可读写
# ds = ogr.Open(shpFile, 1)
# 使用指定的driver打开
driver = ogr.GetDriverByName("ESRI Shapefile")
ds = driver.Open(shpFile, 1)

# 图层个数，一般shp数据图层只有一个，如果是mdb、dxf等图层就会有多个
layCnt = ds.GetLayerCount()

# 第一个图层，要素数量
headLay = ds.GetLayerByIndex(0)
featCnt = headLay.GetFeatureCount()

# 图层定义，字段数量
layDef = headLay.GetLayerDefn()
fldCnt = layDef.GetFieldCount()

for i in range(fldCnt):
  fld = layDef.GetFieldDefn(i)
  print('字段名称 NameRef:', fld.GetNameRef())
  print('字段类型 Type:', fld.GetType())
  print('类型名称 FieldTypeName:', fld.GetFieldTypeName(fld.GetType()))
  print('宽度类型 Width:', fld.GetWidth())

for i in range(featCnt):
  # feat = headLay[i]
  feat = headLay.GetFeature(i)

  # 获取字段值
  idx = feat.GetFieldIndex('Name')
  val = feat.GetField(idx)

  # 更新字段值
  feat.SetField('Name', 'road_' + str(i))
  headLay.SetFeature(feat)
