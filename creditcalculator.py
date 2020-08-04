import math

def calc_months():
  cred_pri = float(input("Enter the credit principal: "))
  mon_pay = float(input("Enter the monthly payment: "))
  cred_int = float(input("Enter the credit interest: "))
  n = float(cred_int/(12*100))
  lg = math.log((mon_pay / (mon_pay - (n * cred_pri))), 1 + n)
  print(lg)
  print(lg/12)
  print(math.ceil(lg)/12)
  if math.ceil(lg) % 12 != 0:
    anos = math.floor(lg / 12)
    meses = math.ceil(lg - (anos * 12))
    print(f"You need {anos} years and {meses} months to repay this credit!")
  if math.ceil(lg) % 12 == 0:
    anos = math.ceil(lg)/12
    print(f"You need {anos} years to repay this credit!")

def calc_ann():
  cred_pri = float(input("Enter the credit principal: "))
  mon_pay = float(input("Enter number of periods: "))
  cred_int = float(input("Enter the credit interest: "))
  n = float(cred_int/(12*100))
  ord_pay = math.ceil(cred_pri * (n*(math.pow((1+n),mon_pay)))/(math.pow((1 + n), mon_pay) - 1))
  print(f"Your annuity payment = {ord_pay}!")

def calc_princ():
  pay_mon = float(input("Enter the monthly payment: "))
  count_per = float(input("Enter the count of periods: "))
  cred_int = float(input("Enter the credit interest: "))
  n = cred_int/(12*100)
  princ_value = math.ceil((pay_mon / ((n * math.pow((1+n),count_per)) / (math.pow((1 + n), count_per) - 1)))) 
  print(f'Your annuity payment = {princ_value}!') 
 


def main():
  print('''What do you want to calculate?
  type "n" for the number of months,
  type "a" for the annuity monthly payment,
  type "p" for the credit principal:''')
  option = str(input()).lower()
  if option == "n":
    calc_months()
  if option == "a":
    calc_ann()
  if option == "p":
    calc_princ()


main()
