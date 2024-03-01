import phonenumbers
from phonenumbers import timezone, geocoder, carrier
#from text import number
import folium



key = "c269a380239f4792bd181e2de37f067b"

number = input("Enter phone number with country code:")
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,"en")
time = timezone.time_zones_for_number(check_number)
car = carrier.name_for_number(check_number,'en')
reg = geocoder.description_for_number(check_number,'en')
print(time)
print(reg)
print(number_location)

from phonenumbers import carrier
service_number = phonenumbers.parse(number)
print(carrier.name_for_number(service_number, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(location=[lat,lng], zoom_start=10)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)

map_location.save("mylocation.html")
