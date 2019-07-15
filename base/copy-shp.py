# -*- coding: utf-8 -*-
from osgeo import ogr, osr
import os,math

# 参考：https://www.cnblogs.com/bobird/articles/3079523.html
driver = ogr.GetDriverByName("ESRI Shapefile")

inshp = '../data/roads.shp'
outputfile = '../data/roads-copy1.shp'

# 获取driver名称，ESRI Shapefile
# driver.GetName()
ds = driver.Open(inshp)
# layer = ds.GetLayerByIndex(0)
layer = ds.GetLayer()

# # (1)基于数据源复制
# if os.access(outputfile, os.F_OK):
#   driver.DeleteDataSource(outputfile)
# dsCopy = driver.CopyDataSource(ds, outputfile)
# # 测试不Release也可以复制
# dsCopy.Release()

# # (2)基于layer复制
# outputfile = '../data/roads_copy2.shp'
# ds2 = driver.CreateDataSource(outputfile)
# # 需要指定图层名
# ds2.CopyLayer(layer, 'abcd')
# ds2.Destroy()

# (3)基于feature复制
outputfile = '../data/roads_copy3.shp'
ds3 = driver.CreateDataSource(outputfile)

if os.access(outputfile, os.F_OK):
  driver.DeleteDataSource(outputfile)
layer3 = ds3.CreateLayer('aaa', None, ogr.wkbLineString)

# 逐个复制feature
# feat = layer.GetNextFeature()
# while feat is not None:
#   layer3.CreateFeature(feat)
#   feat = layer.GetNextFeature()

# 另一种复制方式
featCnt = layer.GetFeatureCount()
for i in range(featCnt):
  feat = layer.GetFeature(i)
  layer3.CreateFeature(feat)

ds3.Destroy()

# 添加同名.prj投影文件
sr = osr.SpatialReference()
sr.ImportFromEPSG(4326)
sr.MorphToESRI()

prjFile = open('../data/roads_copy3.prj', 'w')
prjFile.write(sr.ExportToWkt())
prjFile.close()
