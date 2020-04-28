from math import ceil


# credit_principal = 'Credit principal: 1000'
# final_output = 'The credit has been repaid!'
# first_month = 'Month 1: paid out 250'
# second_month = 'Month 2: paid out 250'
# third_month = 'Month 3: paid out 500'
#
# print(credit_principal,first_month,second_month,third_month,final_output,sep="\n")

def get_int(msg=""):
    while True:
        try:
            return int(input(msg))
        except:
            print("invalid input")




def get_options():
    options="""What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment:
"""
    return input(options)


def get_credit_principal():
    return get_int("Enter the credit   principal: ")

def compute_number_month(credit):
    payment=get_int("Enter monthly payment: ")
    number_month=round(credit/payment)
    return f"It takes {number_month} to repay the credit."

def compute_monthly_payment(credit):
    number_month=get_int("Enter count of months: ")
    payment=ceil(credit/number_month)
    last_payment = credit - payment * (number_month-1)
    msg = f"Your monthly payment = {payment} "
    if last_payment > 0:
        msg += f"with last month payment = {last_payment}"
    return msg

def main():
    credit_principal=get_credit_principal()
    option=get_options()
    if option=="m":
        result=compute_number_month(credit_principal)
    else:
        result=compute_monthly_payment(credit_principal)
    print(result)


main()









