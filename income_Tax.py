"""For example, suppose the taxable income is 45000 the income tax payable is
10000*0% + 10000*10%  + 25000*20% = $6000."""

income = int(input("Input amount of money to calculate the income tax: "))

if income <= 10000:
    incometax = 0
    print("$",incometax)
elif income > 10000 and income <= 20000:
    incometax = 10000 * (10/100)
    print("$",incometax)
else:
    incometax = (10000 * (10 / 100))  + ((income - 20000) *(20/100))
    print("$",incometax)
    #sdfsfsfsf