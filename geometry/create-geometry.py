# -*- coding: utf-8 -*-
from osgeo import ogr
import json

# wktPt = "POINT(116 39)"
# pt = ogr.CreateGeometryFromWkt(wktPt)

# 创建point
pt = ogr.Geometry(ogr.wkbPoint)
pt.AddPoint(116, 39)
# print(pt.GetX(), pt.GetY())

# 创建polyline
pl = ogr.Geometry(ogr.wkbLineString)
pl.AddPoint(116, 39)
pl.AddPoint(116.5, 39)
pl.AddPoint(116.5, 39.5)

# 创建polygon
plr = ogr.Geometry(ogr.wkbLinearRing)
plr.AddPoint(116, 39)
plr.AddPoint(116.5, 39)
plr.AddPoint(116.5, 39.5)
plr.AddPoint(116, 39)

pg = ogr.Geometry(ogr.wkbPolygon)
pg.AddGeometry(plr)

# note: GeoPoint等方法不兼容polygon, Incompatible geometry for operation
for i in range(pl.GetPointCount()):
  # 元组形式
  pt = pl.GetPoint(i)
  print(pt[0], pt[1])
  pass

# 解析json得到点坐标
pgJson = json.loads(pg.ExportToJson())
coords = pgJson['coordinates'][0]

for pt in coords:
  print(pt[0], pt[1])
