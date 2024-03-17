import os
import csv


os.chdir(os.path.dirname(os.path.realpath(__file__)))
FILE_NAME="money.csv"

with open(FILE_NAME,"r",encoding="UTF-8") as f:
    reader = csv.DictReader(f)
    total = 0
    for row in reader:
        total = float(row["Cost"]) * int(row["Quantity"])
    print(f"The total cost is {total:.2f}€")
        