print("Welcome to the BMI Calculator")

height = float(input("enter your height in in m: "))

weight = float(input("enter your weight in kg: "))

BMI = round(weight / height **2)

BMI_as_int = int(BMI)

if BMI_as_int <  18.5:
  print(f"your BMI is {BMI},you are underweight, time to eat a sandwich.")
elif BMI_as_int < 25:
  print(f"your BMI is {BMI}, you are normal weight, keep it up.")
elif BMI_as_int < 30:
  print(f"your BMI is {BMI}, you are overweight, time to hit the gym.")
elif BMI_as_int < 35:
  print(f"your BMI is {BMI}, you are obese, time to cut back on the cake.")
else:
  print(f"your BMI is {BMI}, you are clinically obese, make some drastic changes.")