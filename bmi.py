height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_meters = float(height)
weight_kilograms = int(weight)

bmi = weight_kilograms // (height_meters ** 2)
print(int(bmi))