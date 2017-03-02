#!/usr/bin/python


def kelvinToFahrenheit(temperature):
    assert ((temperature >= 0), "Colder than absolute zero!")
    return ((temperature - 273) * 1.8) + 32


print(kelvinToFahrenheit(273))
print(int(kelvinToFahrenheit(505.78)))
print(kelvinToFahrenheit(-5))
