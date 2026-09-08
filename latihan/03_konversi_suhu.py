celcius = float(input("Suhu dalam Celcius: "))
KELVIN_OOFSET = 273.15
fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + KELVIN_OOFSET
print(f"Fahrenheit: {fahrenheit:.2f} °F")
print(f"Kelvin: {kelvin:.2f} K")