# -*- coding: UTF-8 -*-
#Created by Diego Monge

import arcpy
from arcpy import env
import os
from os import listdir
from googletrans import Translator

project_folder = r'D:\herramientas\ciclones\shp'
env.workspace = project_folder
arcpy.env.overwriteOutput = True

date = datetime.datetime.utcnow().strftime('%Y%m%d')

#rename files
print('rename areas')
for file in arcpy.ListFiles("gtwo_areas*.shp"):
    print(file)
    arcpy.management.Rename(file, 'gtwo_areas.shp')

print('rename lines')
for file in arcpy.ListFiles("gtwo_lines*.shp"):
    print(file)
    arcpy.management.Rename(file, 'gtwo_lines.shp')

print('rename points')
for file in arcpy.ListFiles("gtwo_points*.shp"):
    print(file)
    arcpy.management.Rename(file, 'gtwo_points.shp')

#delete features from server

#deleting points
    """
print("Deleting points")
arcpy.management.DeleteFeatures('https://sig.icafe.cr/server/rest/services/Hosted/Pronostico_de_ciclones/FeatureServer/0')


#deleting lines
print("Deleting lines")
arcpy.management.DeleteFeatures('https://sig.icafe.cr/server/rest/services/Hosted/Pronostico_de_ciclones/FeatureServer/1')
   """   

#deleting polygons
print('Deleting polygons')
arcpy.management.DeleteFeatures('https://sig.icafe.cr/server/rest/services/Hosted/Pronostico_de_ciclones/FeatureServer/2')

#appending data
"""
print('Appending points')
arcpy.Append_management('gtwo_points.shp', 'https://sig.icafe.cr/server/rest/services/Hosted/Pronostico_de_ciclones/FeatureServer/0', 'TEST')

print('Appending lines')
arcpy.Append_management('gtwo_lines.shp','https://sig.icafe.cr/server/rest/services/Hosted/Pronostico_de_ciclones/FeatureServer/1', 'TEST')
"""

print('Appending polygons')
arcpy.Append_management('gtwo_areas.shp', 'https://sig.icafe.cr/server/rest/services/Hosted/Pronostico_de_ciclones/FeatureServer/2', 'TEST')

#get forecast text

h = open(r'D:\herramientas\ciclones\shp\forecast_es.shtml')
	     
html = h.read()
	     
h.close()
	     
print(html)

start_f = html.find("<pre>") + len("<pre>")
end = html.find("</pre>")

forecast_es = html[start_f:end]

text = forecast_es.replace("\n", "</br>")

js = open(r'C:\inetpub\wwwroot\ciclones\forecast_es.js', 'w')
js.write('document.getElementById("forecast").innerHTML = `' + text + '`;')
js.close()

 
