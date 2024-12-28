import csv
import os
fields = ["Decision", "Price", "Amount Dollars","Amount"]
filename = "trades.csv" 

with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

def buy(price,dollars, amt):
     write_to_csv(["BUY", price, dollars, amt])



def sell(price, dollars, amt):
    write_to_csv(["SELL", price,dollars, amt])



def nothing():
    write_to_csv(["HOLD", "-","-", "-"])

    

def write_to_csv(info):
    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)

        # If the file doesn't exist yet, write the header
        if not file_exists:
            csvwriter.writerow(["Decision", "Price", "Amount Dollars","Amount"])

        # Write the actual data row
        csvwriter.writerow(info)
    