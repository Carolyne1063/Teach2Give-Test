'''Write a program that takes an integer as input and returns an integer with reversed digit ordering.'''

def reverse_digits(number):
    return(int(str(number)[::-1]))
user_input= int(input("Enter an integer: "))
result= reverse_digits(user_input)
print("Reversed Number: ", result)