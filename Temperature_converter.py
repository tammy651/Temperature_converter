# Temperature Converter System

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


def celsius_to_kelvin(c):
    return c + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting program...")
        break

    try:
        temp = float(input("Enter temperature value: "))

        if choice == '1':
            print("Result:", celsius_to_fahrenheit(temp), "F")
        elif choice == '2':
            print("Result:", fahrenheit_to_celsius(temp), "C")
        elif choice == '3':
            print("Result:", celsius_to_kelvin(temp), "K")
        elif choice == '4':
            print("Result:", kelvin_to_celsius(temp), "C")
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number")