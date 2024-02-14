

# write a fuction for calculating BMI. User should be able to input their weight and height.

# smome comment


# configuration code

# some more comment

# some more comment

def calculate_bmi(weight, height):
   # write docstring

    """
    This function calculates the BMI of a person.
    weight: weight of the person in kg
    height: height of the person in meters
    """   

    bmi = weight / (height ** 2)
    return bmi


def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi}")