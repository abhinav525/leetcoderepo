import csv
from prettytable import PrettyTable
with open("Employee.csv") as CSVR:#CSVR is file handler which is variable name
    emp_details=csv.reader(CSVR)
    #colnames=next(emp_details)
    prtbl=PrettyTable(next(emp_details))
    #print(colnames)
    for rec in emp_details:
        prtbl.add_row(rec)
    print(prtbl)


