#Financial Wellness & Savings Target Calculator

# User Info 
Name = input("Enter Your Name : ")

#Basic Account and Finances Info 
Monthly_Income = float(input("Monthly Income ($): "))
Fixed_Expenses = float(input("Fixed Expenses ($) : "))
Savings_Goal = float(input("Saving Goals ($) : "))
Days = 30

# Arithmetic operations to perform for calculations
Remaining_Disposable_Income = Monthly_Income - Fixed_Expenses - Savings_Goal
Daily_Budget = (Monthly_Income - Fixed_Expenses - Savings_Goal) / Days
Actual_savings = Monthly_Income - Fixed_Expenses
Expense_to_Income_Ratio = (Fixed_Expenses / Monthly_Income) * 100

# Logical Function to see person in safe spending zone
Goal_Attained = Actual_savings>= Savings_Goal
Safe_Zone = Expense_to_Income_Ratio<= 50.0


#Results

print("=" * 50)
print("               FINANCIAL SUMMARY             ")
print("=" * 50)
print("User Name : " , Name)
print("-" * 50)
print("Monthly Income ($) :          " ,Monthly_Income)
print("Fixed Expenses ($) :          " ,Fixed_Expenses)
print("Savings Goal ($) :            " ,Savings_Goal)
print("Remaining Income ($) :        ", Remaining_Disposable_Income)
print("Daily Budget ($) :            ", Daily_Budget)
print("Expense-to-Income Ratio :     " , Expense_to_Income_Ratio)
print("Safe Spending ($) :           " , Safe_Zone)
print("-" * 50)

