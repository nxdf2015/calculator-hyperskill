from math import ceil,log


# credit_principal = 'Credit principal: 1000'
# final_output = 'The credit has been repaid!'
# first_month = 'Month 1: paid out 250'
# second_month = 'Month 2: paid out 250'
# third_month = 'Month 3: paid out 500'
#
# print(credit_principal,first_month,second_month,third_month,final_output,sep="\n")

def get_float(msg=""):
    while True:
        try:
            return float(input(msg))
        except:
            print("invalid input")




def get_options():
    options="""What do you want to calculate? 
type "n" - for count of months,
type "a" - for annuity monthly payment,
type "p" - for credit principal:
"""
    return input(options)


# def get_credit_principal():
#     return get_float("Enter the credit   principal: ")

def compute_number_month(credit):
    payment=get_float("Enter monthly payment: ")
    interest = float(input("Enter credit interest: ")) / 1200
    count  = ceil(log( payment /  ( payment - interest * credit), interest + 1))
    print(count)
    years = count // 12
    months = count  %12
    msg = "You need "
    if years > 0 :
        msg += str(int(years))+f" year{'s' if years > 1 else '' } "
    if months > 0:
        if years > 0 :
            msg += "and "
        msg += str(ceil(months)) + " months "
    msg += "to repay this credit!"
    return msg



def compute_annuity_monthly_payment(credit):
    periods = int(input("Enter count of periods:"))
    interest = float(input("Enter credit interest: ")) / 1200
    annuity = ceil(credit * (interest  * ( 1 + interest) ** periods) / ((1 + interest )**periods -1))
    return f"Your annuity payment = {annuity}!"

# def compute_monthly_payment(credit):
#     number_month=get_int("Enter count of months: ")
#     payment=ceil(credit/number_month)
#     last_payment = credit - payment * (number_month-1)
#     msg = f"Your monthly payment = {payment} "
#     if last_payment > 0:
#         msg += f"with last month payment = {last_payment}"
#     return msg

def get_credit_principal():
    return  float (input("Enter credit principal: "))

def compute_credit_principal():
    payment = float(input("Enter monthly payment"))
    periods = int(input("Enter count of periods"))
    interest  = float(input("Enter credit interest")) /1200
    credit= payment / (( interest * (1 + interest) ** periods ) / ( (1 + interest) ** periods  - 1))
    return f"Your credit principal = {credit}!"

def main():
    option=get_options()
    if option=="n":
        credit_principal = get_credit_principal()
        result=compute_number_month(credit_principal)
    elif option == "a":
        credit_principal = get_credit_principal()
        result=compute_annuity_monthly_payment(credit_principal)
    elif option=="p":
        result = compute_credit_principal()

    print(result)


main()









