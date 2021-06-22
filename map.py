import folium
import pandas


# Get volcano data
data = pandas.read_csv("Volcanoes.txt")


lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# Initialize Map
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")


# Helper function to determine marker color
def color_producer(el):
    if el < 1000:
        return 'green'
    elif 100 <= el < 3000:
        return 'orange'
    else:
        return 'red'

# Add markers to map
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup((str(el) + " m"), parse_html=True), 
   fill_color=(color_producer(el)), color = 'grey', fill_opacity=.7 ))

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
 style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' 
 if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")