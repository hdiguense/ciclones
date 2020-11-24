
$url = "https://www.nhc.noaa.gov/xgtwo/gtwo_shapefiles.zip"
$output = "D:\herramientas\ciclones\gtwo_shapefiles.zip"

Invoke-WebRequest -Uri $url -OutFile $output

#clean shp files
Write-Host "removing all files"
Remove-Item D:\herramientas\ciclones\shp\* -Recurse -Force
#Unzip
write-host "unziping"
Expand-Archive D:\herramientas\ciclones\gtwo_shapefiles.zip -DestinationPath D:\herramientas\ciclones\shp -Force

write-host " Download spanish forecast" 
Invoke-WebRequest -Uri https://www.nhc.noaa.gov/text/SJUTWOSP.shtml -OutFile D:\herramientas\ciclones\shp\forecast_es.shtml
#run python script
Write-Host "runing python"
Start-Process 'D:\herramientas\ciclones\env_ciclones\python.exe' 'D:\herramientas\ciclones\ciclones.py'