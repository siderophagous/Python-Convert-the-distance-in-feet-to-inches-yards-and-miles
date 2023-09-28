
# Define a dictionary for conversion factors with user-friendly unit names
conversion_factors = {
    "cm_to_m": ("Centimeters to Meters", 0.01),
    "mm_to_cm": ("Millimeters to Centimeters", 0.1),
    "m_to_cm": ("Meters to Centimeters", 100),
    "cm_to_mm": ("Centimeters to Millimeters", 10),
    "m_to_mm": ("Meters to Millimeters", 1000),
    "km_to_m": ("Kilometers to Meters", 1000),
    "m_to_km": ("Meters to Kilometers", 0.001),
    "mm_to_km": ("Millimeters to Kilometers", 0.000001),
    "ft_to_cm": ("Feet to Centimeters", 30.48),
    "ft_to_mm": ("Feet to Millimeters", 304.8),
    "ft_to_inch": ("Feet to Inches", 12),
    "inch_to_cm": ("Inches to Centimeters", 2.54),
    "inch_to_mm": ("Inches to Millimeters", 25.4),
}

# Display the list of conversion options to the user
print("Select a conversion option:")
for index, (conversion_desc, _) in enumerate(conversion_factors.values(), start=1):
    print(f"{index}. {conversion_desc}")

# Prompt the user to choose a conversion option
choice = int(input("Enter the number of your choice: "))

# Ensure the user's choice is within a valid range
if 1 <= choice <= len(conversion_factors):
    # Get the selected conversion key and its conversion factor
    conversion_key, (_, conversion_factor) = list(conversion_factors.items())[choice - 1]

    # Input from the user
    num1 = float(input('Enter the value: '))

    # Perform the conversion
    ans = num1 * conversion_factor
    print(ans)
else:
    print("Invalid choice. Please select a valid conversion option.")
