import folium
import pandas

file = pandas.read_csv("Volcanoes.txt")
lat = list(file['LAT'])
lon = list(file['LON'])
elev = list(file['ELEV'])

def colour_producer(elevation):
    if elevation < 1000:
         return 'green'
    elif  1000 <= elevation < 2000:
         return 'orange'
    else:
         return 'red'

map = folium.Map(location=[38.58,-99.09],zoom_Start = 6,titles='Stamen terrain')

fgv = folium.FeatureGroup(name="My Map")

for lt, ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.Marker(location = [lt,ln],popup = el,icon = folium.Icon(color=colour_producer(el))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")