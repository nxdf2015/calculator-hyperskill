from math import ceil,log
from sys import argv

class Parser :
    def __init__(self,arg=[]):
        self.args = arg
        self.arguments= {}


    def parse(self):


        if not len(self.args) % 2 == 0:
            return "Incorrect parameters"
        else:
            for  data  in  self.args:

                if data[:2] == "--":
                    key,value = data[2:].split("=")
                    if not key == "type":
                        value = float(value)
                    self.arguments[key]=value
                else:
                    continue

        return self.valid()

    def valid(self):
        if not "interest" in self.arguments:
            return False
        if not "type" in self.arguments:
            return False
        if self.arguments["type"]=="diff":
            return len(self.arguments)== 4 and not "payment" in self.arguments
        else:
            return len(self.arguments) == 4

    def selection(self):
        if self.arguments["type"] == "diff":
            return "diff"
        else:
            options ="payment principal periods type".split(" ")
            for key in options:
                if not key in self.arguments:
                    return key


    def __getitem__(self, item):
        return self.arguments[item]


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




def compute_number_month(credit,payment,interest):
    count  = ceil(log( payment /  ( payment - interest * credit), interest + 1))
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
    print(msg)
    print()
    print(f"Overpayment = {payment * count - credit}")



def compute_annuity_monthly_payment(credit,periods,interest):
    annuity = ceil(credit * (interest  * ( 1 + interest) ** periods) / ((1 + interest )**periods -1))
    print( f"Your annuity payment = {periods * annuity - credit}!")
    print()
    print(f"Overpayment = {annuity}")


def get_credit_principal():
    return  float (input("Enter credit principal: "))

def compute_credit_principal(payment,periods,interest):
    credit= round(payment / (( interest * (1 + interest) ** periods ) / ( (1 + interest) ** periods  - 1)))

    print( f"Your credit principal = { periods * payment - credit}!")
    print()
    print(f"Overpayment = {credit}")


def parse_arg():
    if len(argv[1:]) % 2 == 0:
        return "Incorrect parameters"


def compute_differential(principal, periods, interest):
    d = lambda i : ceil((principal/ periods )+ interest * ( principal * ( 1 -  ( i - 1 )  / periods)))
    values= [ d(i) for i in range(1,int(periods)+1)]
    total = sum(values)
    for i,value in enumerate(values):
         print(f"Month {i+1}: paid out {d(i+1)}")
    overpayment = total - principal
    print(f"Overpayment = {overpayment}")



def application():

    arguments = argv[1:]
    parser = Parser(arguments)
    parser.parse()

    if not parser.valid():
        print("incorrect parameters")
    else:
        selection = parser.selection()
        # print(selection)
        interest = parser["interest"] / 1200
        if selection == "diff":
            compute_differential(parser["principal"],parser["periods"],interest)
        else:
            if selection == "periods":
                payment = parser["payment"]
                credit = parser["principal"]
                compute_number_month(credit,payment,interest)

            elif selection == "principal":
                periods = parser["periods"]
                payment = parser["payment"]
                compute_credit_principal(payment,periods,interest)

            elif selection == "payment":
                principal = parser["principal"]
                periods = parser["periods"]
                compute_annuity_monthly_payment(principal,periods,interest)


application()










