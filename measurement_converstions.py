# How to convert feet to inches to meters for height.
# To convert feet to inches * by 12 
# To convert inches to meters we need to * inches by 0.0254 meters
print('Convert your height to Meters. ')
feet_to_inches = 12
inches_to_meters = 0.0254
feet = int(input('Feet: '))
inches = int(input('Inches: '))
height_in_meters = (feet * feet_to_inches + inches) * inches_to_meters

print(height_in_meters)


