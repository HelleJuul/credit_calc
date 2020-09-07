credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

#print(credit_principal)
#print(first_month)
#print(second_month)
#print(third_month)
#print(final_output)


print("Enter the credit principal: ")
principal = int(input())

print("What do you want to calculate?")
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payment:')
calc_type = input()
if calc_type == "m":
    print("Enter the monthly payment:")
    monthly_payment = int(input())

    if monthly_payment == principal:
        print("It will take 1 month to repay the credit")

    elif principal % monthly_payment == 0:
        months = principal // monthly_payment
    else:
        months = principal // monthly_payment + 1

    print(f"\nIt will take {months} months to repay the credit ")

elif calc_type == "p":
    print("Enter the number of months:")
    months = int(input())

    if principal % months == 0:
        monthly_payment = principal // months
        print(f"\nYour monthly payment = {monthly_payment}")
    else:
        monthly_payment = principal // months + 1
        last_payment = principal - (months - 1) * monthly_payment
        print(f"\nYour monthly payment = {monthly_payment} and the last payment = {last_payment}.")
