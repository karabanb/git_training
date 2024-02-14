

# write a fuction for calculating BMI. User should be able to input their weight and height.

# smome comment

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi}")