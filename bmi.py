weight = input("Enter your weight(kg)")
height = input("Enter your height(m)")

weight = float(weight)
height = float(height)

bmi = weight/(height*height)

if bmi <= 18:
    print("Underweight")
elif bmi <= 29:
    print("Normal weight")
elif bmi <= 34:
    print("Overweight")
else:
    print("Obese")

print("your BMI", bmi)
