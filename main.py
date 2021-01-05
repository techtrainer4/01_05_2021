bill = 55.66 #float = floating point decimal = decimal 
no_ppl = 5
share = bill / no_ppl
print(share)  
print("Each person owes ${:.2f}.".format(share))

def BillCalc():
  Bill = input("How much was your bill?")
  Bill = float(Bill)
  Ppl = input("How many people are splitting this?")
  Ppl = int(Ppl)
  Share = Bill / Ppl
  return "Each person owes ${:.2f}.".format(Share)

print(BillCalc())

def email_assigner():
  fname = input("What is your first name?")
  lname = input("What is your last name?")
  cname = "@something.com"
  return "{}.{}{}".format(fname,lname,cname)

print(email_assigner())




  









