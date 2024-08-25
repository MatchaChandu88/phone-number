import phonenumbers
from test import number
from phonenumbers import geocoder
ch_nmber=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber,"en"))


phone=phonenumbers.parse("+919010383088")
valid=phonenumbers.is_valid_number(phone) 
print(phone)
print(valid)


from phonenumbers import timezone
timeZone=timezone.time_zones_for_number(phone)
print(timeZone)

from phonenumbers import carrier
service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))