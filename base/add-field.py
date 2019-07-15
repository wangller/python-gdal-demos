# -*- coding: utf-8 -*-
from osgeo import ogr, osr
import os,math

# 参考：https://www.cnblogs.com/bobird/articles/3079523.html
driver = ogr.GetDriverByName("ESRI Shapefile")

inshp = '../data/roads.shp'

ds = driver.Open(inshp)
layer = ds.GetLayerByIndex(0)

outputfile = '../data/roads_copy3.shp'
ds3 = driver.CreateDataSource(outputfile)

if os.access(outputfile, os.F_OK):
  driver.DeleteDataSource(outputfile)
layer3 = ds3.CreateLayer('roads_copy3', None, ogr.wkbLineString)

# 添加Name字段
fldName = ogr.FieldDefn('Name', ogr.OFTString)
fldName.SetWidth(20)
layer3.CreateField(fldName)
# 添加Count字段
layer3.CreateField(ogr.FieldDefn('Count'), ogr.OFTInteger)

# 逐个复制feature
feat = layer.GetNextFeature()
while feat:
  geom = feat.geometry()
  # newFeat = feat.Clone()
  newFeat = ogr.Feature(layer3.GetLayerDefn())
  newLine = ogr.Geometry(ogr.wkbLineString)
  newFeat.SetField(0, feat.GetField('Name'))
  newFeat.SetField(1, 10)

  for i in range(geom.GetPointCount()):
    pt = geom.GetPoint(i)
    newLine.AddPoint(pt[0], pt[1] + 0.001)

  newFeat.SetGeometry(newLine)
  layer3.CreateFeature(newFeat)
  feat = layer.GetNextFeature()

# 添加同名.prj投影文件
sr = osr.SpatialReference()
sr.ImportFromEPSG(4326)
sr.MorphToESRI()

prjFile = open('../data/roads_copy3.prj', 'w')
prjFile.write(sr.ExportToWkt())
prjFile.close()
