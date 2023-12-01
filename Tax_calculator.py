# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:54:44 2023
Program_04
@author: Bradley Sheldon
"""

# Function to calculate adjusted gross income (AGI)
def calc_AGI(wages, interest, unemployment):
    return wages + interest + unemployment

# Function to calculate total deductions based on status
def calc_deductions(status):
    if status == 0:
        return 6000
    elif status == 1:
        return 12000
    else:
        return 24000

# Function to calculate taxable income
def calc_taxable_income(AGI, deductions):
    taxable_income = AGI - deductions
    if taxable_income < 0:
        return 0
    else:
        return taxable_income

# Function to calculate tax owed
def calc_tax_owed(status, taxable_income, taxes_withheld):
    if status == 0 or status == 1:
        if taxable_income <= 10000:
            tax_owed = taxable_income * 0.1
        elif taxable_income <= 40000:
            tax_owed = 1000 + (taxable_income - 10000) * 0.12
        elif taxable_income <= 85000:
            tax_owed = 4600 + (taxable_income - 40000) * 0.22
        else:
            tax_owed = 14500 + (taxable_income - 85000) * 0.24
    else:
        if taxable_income <= 20000:
            tax_owed = taxable_income * 0.1
        elif taxable_income <= 80000:
            tax_owed = 2000 + (taxable_income - 20000) * 0.12
        else:
            tax_owed = 9200 + (taxable_income - 80000) * 0.22
    tax_owed -= taxes_withheld
    return tax_owed

# Main code (body)
# Asks user to input info.
wages = float(input("Enter total yearly wages earned: $"))
interest = float(input("Enter total interest earned: $"))
unemployment = float(input("Enter total unemployment compensation: $"))
status = int(input("Enter status (0=dependent, 1=single, or 2=married): "))
taxes_withheld = float(input("Enter taxes already withheld: $"))

AGI = calc_AGI(wages, interest, unemployment)
deductions = calc_deductions(status)
taxable_income = calc_taxable_income(AGI, deductions)
tax_owed = calc_tax_owed(status, taxable_income, taxes_withheld)

# Prints output
print("\n\nResults in the following data:\n")
print("AGI: $" + str(AGI), "(",str(wages),"+",str(interest),"+",str(unemployment),")")
print("Deductions: $" + str(deductions))
print("Amount of taxable income: $" + str(taxable_income), "(",str(AGI),"-",str(deductions),")")
print("Tax owed: $" + str(tax_owed))
