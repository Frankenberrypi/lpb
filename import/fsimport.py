import psycopg2
import shapefile
import sys

conn = psycopg2.connect("dbname='osm' user='postgres' host='localhost' password='postgres' port='5433'")
cursor = conn.cursor()

sf=shapefile.Reader(sys.argv[1])
shapes=sf.iterShapes()


for i in range(0, sf.numRecords):
    shape = shapes.next()

    geometry = []
    for point in shape.points:
        geometry.append(str(point[0]) + " " + str(point[1]))

    cursor.execute("insert into fsline (geom) values(st_geomfromtext('LINESTRING(" + ", ".join(geometry) + ")', 4326))")

conn.commit()