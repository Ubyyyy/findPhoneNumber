import phonenumbers
from time import time
from numpy import number
from phonenumbers import timezone, geocoder, carrier
number = input("Scrie numarul de telefon aici: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "ro")
reg = geocoder.description_for_number(phone, "ro")

print(phone)
print(time)
print(car)
print(reg)

