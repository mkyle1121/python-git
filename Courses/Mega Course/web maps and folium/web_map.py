import folium
import pandas

df1 = pandas.read_csv('Volcanoes_USA.txt')
print (df1.columns)   #print column headers

print (df1['LAT'])    # print all items in a column

lat = list(df1['LAT'])
lon = list(df1['LON'])
elev = list(df1['ELEV'])

def color_producer(l):
    if l < 1000:
        return 'green'
    elif l <= 2000:
        return 'orange'
    else:
        return 'red'


print (lat)
print (lon)

map = folium.Map(location=[30, -100], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name='Volcanoes')
# map.add_child(folium.Marker(location=[38.2, -99.1], popup='Hi I am a marker', icon=folium.Icon(color='green')))
fgv.add_child(folium.Marker(location=[38.2, -99.1], popup='Hi I am a marker', icon=folium.Icon(color='green')))
fgv.add_child(folium.Marker(location=[40.2, -95.1], popup='Hi I am a marker', icon=folium.Icon(color='green')))
fgv.add_child(folium.Marker(location=[37.2, -97.1], popup='Hi I am a marker', icon=folium.Icon(color='green')))

#########3 populate the field markers
for lt, ln, l in zip(lat, lon, elev):
    #fg.add_child(folium.Marker(location=[lt, ln], popup=str(l), icon=folium.Icon(color=color_producer(l))))
    fgv.add_child((folium.CircleMarker(location=[lt,ln], popup=str(l), color=color_producer(l), fill=True, fill_opacity=.5 )))


for coordinates in [[37,-95],[35,-85]]:
    fgv.add_child(folium.Marker(location=coordinates, popup='Hi I am a marker', icon=folium.Icon(color='green')))


fgp = folium.FeatureGroup(name='Population')


fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']  < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)


map.add_child(folium.LayerControl())


map.save('Map1.html')
