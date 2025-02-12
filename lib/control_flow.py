def admin_login(username, password):
    """
    Checks if the provided username and password match the admin credentials.

    Args:
        username: The username to check.
        password: The password to check.

    Returns:
        "Access granted" if the username is "admin" or "ADMIN" and the password is "12345".
        "Access denied" otherwise.
    """
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    """
    Determines the weather description based on the given temperature.

    Args:
        temperature: The temperature in degrees.

    Returns:
        "It's brisk out there!" if the temperature is below 40.
        "It's a little chilly out there!" if the temperature is between 40 and 65 (inclusive).
        "It's too dang hot out there!" if the temperature is above 85.
        "It's perfect out there!" otherwise.
    """
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(number):
    """
    Applies the FizzBuzz logic to a given number.

    Args:
        number: The number to check.

    Returns:
        "Fizz" if the number is a multiple of 3.
        "Buzz" if the number is a multiple of 5.
        "FizzBuzz" if the number is a multiple of both 3 and 5.
        The number itself otherwise.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


def calculator(operation, num1, num2):
    """
    Performs a calculation based on the given operation and numbers.

    Args:
        operation: The operation to perform (+, -, *, /).
        num1: The first number.
        num2: The second number.

    Returns:
        The result of the operation if it's valid.
        "Invalid operation!" and None if the operation is not valid.
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None