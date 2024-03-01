# loan = 1.000 $
# pro jahr +5%
# gesamt wert für 10 jahre


loan = 1000
interest = (loan * 5) / 100

for number in range(10):
    loan = loan + interest
    print(f"Your total on Year {number+1} is {round(loan,2)}\n")
