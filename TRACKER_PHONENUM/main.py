import phonenumbers
import opencage
import folium
from myphone import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

pepnumber = phonenumbers.parse(number)
# locating the country
location = geocoder.description_for_number(pepnumber,"en")
print(location)

# service = phonenumbers.parse(number)
service_pro = carrier.name_for_number(pepnumber,"en") 
print(service_pro) # carrier_network name


key = '1a816e625dc043409360fa36ddbaf81c'

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
# print(result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
# print(lat,lng)

mymap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(mymap)
mymap.save("Location.html")