import math

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type", help="select between differentiate payment: 'diff' and annuity payment: 'annuity'")

parser.add_argument("--payment", type=int, help="the monthly payment")

parser.add_argument("--principal", type=int, help="the credit principal")

parser.add_argument("--periods", type=int, help="the number of payments to repay the credit")

parser.add_argument("--interest", type=float, help="the yearly interest as percent; no percentage sign")

args = parser.parse_args()



def calculate_number_of_payments(principal, payment, interest):
    """Calculate the number of payments needed to repay a loan given a credit
    principal, a monthly payment and an annual interest"""

    P = principal
    A = payment

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

    calculate_overpayment(P, n, A)



def calculate_principal(payment, periods, interest):
    """Calculate the principal given the monthly payment, the total number of
    payments and the annual interest."""
    
    A = payment
    n = periods
   
    # Calculate the monthly interest as a decimal number
    i = (interest / 100) / 12

    # Calculate the principal credit
    P = A / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
    
    print(f"Your credit principal = {round(P)}!")
    
    calculate_overpayment(round(P), n, A)



def calculate_payment(principal, periods, interest):
    """Calculate the monthly payment given the credit principal, the total 
    number of payments and the annual interest."""

    P = principal
    n = periods

    # Calculate the monthly interest as a decimal number
    i = (interest / 100) / 12

    # Calculate the monthly payments
    A = P * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)

    print(f"Your monthly payment = {math.ceil(A)}!")

    calculate_overpayment(P, n, math.ceil(A))


def calculate_overpayment(principal, periods, payment):
    """Calculate how much much it cost you to take the loan"""

    overpayment = periods * payment - principal

    print(f"Overpayment = {overpayment}")


def calculate_differentiated_payments(principal, periods, interest):
    """Calculate and print the differentiated payments"""

    P = principal
    n = periods

    # calculate the monthly interest as a decimal number
    i = (interest / 100) / 12

    total_payments = 0

    # The monthly payment is called D
    for m in range(1, n + 1):
        D = P / n + i * (P - P * (m - 1) / n)

        total_payments += math.ceil(D)

        print(f"Month {m}: payment is {math.ceil(D)}")
    
    print(f"\nOverpayment = {round(total_payments - P)}")



# Check how many arguments have been given when starting the program
# And checking that no arguments are negative.
count = 0
if args.type:
    count += 1
if args.payment:
    if args.payment <= 0:
        print("Incorrect parameters")
    count += 1
if args.principal:
    if args.principal <= 0:
        print("Incorrect parameters")
    count += 1
if args.periods:
    if args.periods <= 0:
        print("Incorrect parameters")
    count += 1
if args.interest:
    if args.interest <= 0:
        print("Incorrect parameters")
    count += 1


if count < 4:                     
    print("Incorrect parameters")

else:
    if args.type == "diff":
        if args.payment:
            print("Incorrect parameters")
        else:
            calculate_differentiated_payments(args.principal, args.periods, args.interest)

    elif args.type == "annuity":
        if not args.interest:
            print("Incorrect parameters")
        elif not args.periods:
            calculate_number_of_payments(args.principal, args.payment, args.interest)

        elif not args.principal:
            calculate_principal(args.payment, args.periods, args.interest)

        elif not args.payment:
            calculate_payment(args.principal, args.periods, args.interest)

    else:
        print("Incorrect parameters")


