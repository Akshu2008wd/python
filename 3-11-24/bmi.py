height=float(input("Enter your height: "))
weight=float(input("Enter your weight: "))

bmi=weight/(height/100)**2
print(f"Your BMI is {bmi}")

if(bmi<18.5):
    print("Underweight")
elif(bmi<25):
    print("Normal")
elif(bmi<30):
    print("Overweight")
else:
    print("Obese")