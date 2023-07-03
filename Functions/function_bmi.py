def bmi_calculator():
    height = float(input("Enter Your Height"))
    weight = float(input("Enter Your Weight"))
    bmi = weight / (height * height)
    print(f"Your BMI is {bmi}")
bmi_calculator()

