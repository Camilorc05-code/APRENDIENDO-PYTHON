### Python Package Manager ###

# PIP3 https://pypi.org

import numpy # pip3 install numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 32, 20, 11, 15])
print(type(numpy_array))

print(numpy_array * 2)

import pandas # pip3 install pandas

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))
