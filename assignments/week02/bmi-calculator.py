#Assignment : BMI Calculator

#Input
weight = float(input("Input you weight(KG) : "))
height = float(input("Input you height(M) : "))
#Process
bmi = weight / (height ** 2)
#output
print(f"\nBMI = {bmi:.1f}")
#if-else
if bmi <= 18.5:
    cate = "Underweight"
elif bmi <= 24.9:
    cate = "Normal weight"
elif bmi <= 29.9:
    cate = "Overweight"
else:
    cate = "Obese"
print("\n" + "=" * 40 + "\n")
print(cate)