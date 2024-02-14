

# write a fuction for calculating BMI. User should be able to input their weight and height.


def calculate_bmi(weight, height):
   # write docstring

    """
    This function calculates the BMI of a person.
    weight: weight of the person in kg
    height: height of the person in meters
    """   

    bmi = weight / (height ** 2)
    return bmi
