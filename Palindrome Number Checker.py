def is_palindrome(num):
    original = str(num)
    reverse = original[::-1]

    if original == reverse:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if is_palindrome(number):
    print(number, "is a Palindrome Number")
else:
    print(number, "is not a Palindrome Number")2