from osgeo import ogr, osr

souSr = osr.SpatialReference()
souSr.ImportFromEPSG(4326)

tarSr = osr.SpatialReference()
tarSr.ImportFromEPSG(3857)

ct = osr.CoordinateTransformation(souSr, tarSr)
pt = ogr.CreateGeometryFromWkt("POINT (113.256774 35.185013)")

# pt = ogr.Geometry(ogr.wkbPoint)
# pt.AddPoint(113.256774, 35.185013)

# 12607686.452 4189052.1469

pt.Transform(ct)
# note: 结果是无限大inf
print(pt.GetX())

# print(souSr.ExportToWkt())
# print(souSr.ExportToProj4())

# # print(souSr.GetAxisName())
# print(souSr.GetInvFlattening())
# print(souSr.IsGeographic())
# print(souSr.IsGeocentric())

# print(tarSr.IsGeographic())
# print(tarSr.IsGeocentric())
