import math

# A = annuity payment
# P = credit principal
# i = nominal (monthly) interest rate. Is a floating value (not percent)
# n = number of payments (i.e. number of months)

print("What do you want to calculate?")
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for credit principal:')

answer = input()

if answer == "n":       # We want to calculate n
    print("Enter the credit principal:")
    P = float(input())
    print("Enter the monthly payment:")
    A = float(input())
    print("Enter the credit interest:")
    interest = float(input())

    # calculate the monthly interest rate as a decimal number
    i = (interest / 100) / 12

    # calculate the number of payments
    n_decimal = math.log(A / (A - i * P), 1 + i)

    # round up to the nearest integer
    n = math.ceil(n_decimal)

    # create the output in years and months
    if n == 1:
        print(f"It will take 1 month to repay this credit!")
    elif n < 12:
        print(f"It will take {n} months to repay this credit!")
    elif n == 12:
        print(f"It will take 1 year to repay this credit!")
    elif n < 24:
        months = n % 12
        print(f"It will take 1 year and {months} months to repay this credit!")
    else:
        years = n // 12
        months = n % 12
        print(f"It will take {years} years and {months} months to repay this credit!")


elif answer == "a":     # We want to calculate A
    print("Enter the credit principal:")
    P = float(input())
    print("Enter the number of periods:")
    n = int(input())
    print("Enter the credit interest:")
    interest = float(input())

    # Calculate the monthly interest as a decimal number
    i = (interest / 100) / 12

    # Calculate the monthly payments
    A = P * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)

    print(f"Your monthly payment = {math.ceil(A)}!")

elif answer == "p":     # We want to calculate P
    print("Enter the annuity payment:")
    A = float(input())
    print("Enter the number of periods:")
    n = int(input())
    print("Enter the credit interest:")
    interest = float(input())

    # Calculate the monthly interest as a decimal number
    i = (interest / 100) / 12

    # Calculate the principal credit
    P = A / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))

    print(f"Your credit principal = {round(P)}!")
