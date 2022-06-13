from typing import List


def digit_list_to_value(digits: List[int]) -> int:
    # First, we validate (assuming it is a list of integers) that the caller's input is a list of digits.
    if not all(0 <= digit <= 9 for digit in digits):
        raise ValueError("Input digits list must contain only valid digits")

    # We set the variable "value" to initially be zero, and then sum over each element in the list of
    # digits (multiplied by their place value). Python lists are 0-indexed, which means for some element
    # digits[index], the place-value can be given by 10, raised to the power of 'len(digits) - index - 1'.
    value: int = 0
    for index in range(len(digits)):
        value += pow(10, len(digits) - index - 1) * digits[index]

    # Return the result to the caller.
    return value


def main() -> None:
    # The 'input' function prints a message and then asks the user for input.
    user_input: str = input("Input a comma-separated list of integers: ")
    try:
        # We strip whitespace from the user input, split it by commas, and then
        # map each value in the resulting list to the result of applying
        # the 'int' function on it, to interpret that string as an integer.
        parsed_input: List[int] = list(map(int, user_input.strip().split(',')))
        result: int = digit_list_to_value(parsed_input)
        print(f"Your number is: {result}")
    except ValueError as e:
        print(f"There was an issue with your input: {e}. Please try again.")


# This is the entry-point of the program when the python interpreter executes this script.
if __name__ == "__main__":
    main()
