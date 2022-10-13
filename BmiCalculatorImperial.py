#BMI Index Calculator Imperial
gender = input("Are you Male or Female? Male/Female ").lower()
weight = input("Enter your weight in pounds: ")
height = input("Enter your height in inches: ")
bmi = int(weight) / int(height) ** 2 * 703
# weight (lb) / [height (in)] 2 x 703
#categorize bmi status
if bmi <= 18.4:
  print(f"Your bmi is: {bmi}, you are underweight. ")
elif bmi <= 18.5:
  print(f"Your bmi is {bmi}, you are a normal weight. ")
elif bmi <25:
 print(f"Your bmi is {bmi}, you are overweight. ")
elif bmi <30:
  print(f"Your bmi is{bmi}, you are, by definition, obese class 1. ")
elif bmi <35:
  print(f"Your bmi is {bmi}, you are, by definition, obsese class 2. ")
elif bmi <40:
  print(f"Your bmi is {bmi}, you are, by definition, obese class 3. ")