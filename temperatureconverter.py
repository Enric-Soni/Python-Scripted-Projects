from_scale = input("Enter the scale from which you want to convert the temperature! Your choices are C, F, and K! * UPPERCASE ONLY *\n")
to_scale = input("Enter the scale to which you want to convert the temperature!\n")
if from_scale not in "CFK" or to_scale not in "CFK":
  raise ValueError("Invalid scale selected")
if from_scale == to_scale:
  raise ValueError("Both the scales cannot be the same.")
temp = float(input("Enter the temperature\n"))
if from_scale == "C":
  if to_scale == "F":
    final = (1.8 * temp) + 32
    print(f"{temp} degrees Celsius is {final} degrees Fahrenheit.!")
  elif to_scale == "K":
    final = temp + 273.15
    print(f"{temp} degrees Celsius is {final} degrees Kelvin.!")
if from_scale == "F":
  if to_scale == "C":
    final = (temp - 32) / 1.8
    print(f"{temp} degrees Fahrenheit is {final} degrees Celsius!")
  elif to_scale == "K":
    final = (temp - 32) / 1.8 + 273.15
    print(f"{temp} degrees Fahrenheit is {final} degrees Kelvin!")
if from_scale == "K":
  if to_scale == "C":
    final = temp - 273.15
    print(f"{temp} degrees Kelvin is {final} degrees Celsius!")
  if to_scale == "F":
    final = (1.8 * (temp - 273.15)) + 32
    print(f"{temp} degrees Kelvin is {final} degrees Fahrenheit!")