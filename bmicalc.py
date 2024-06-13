def calculate_bmi(weight_pounds, height_inches):
    """Calculate the BMI given weight in pounds and height in inches."""
    # Convert weight from pounds to kilograms (1 pound = 0.453592 kilograms)
    weight_kg = weight_pounds * 0.453592
    # Convert height from inches to meters (1 inch = 0.0254 meters)
    height_m = height_inches * 0.0254
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    """Determine the BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator")
    weight_pounds = float(input("Enter your weight in pounds: "))
    height_inches = float(input("Enter your height in inches: "))
    
    bmi = calculate_bmi(weight_pounds, height_inches)
    category = bmi_category(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are categorized as: {category}")


main()
