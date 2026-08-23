#Reciept Basic Information
Customer_name = input("Customer Name : ")
Customer_ID = input("Customer ID : ")
Counter_No = int(input("Counter No : "))
Product_Name = input("Product Name : ")
Product_Qty = float(input("Product Qty : "))
Unit_Price = float(input("Unit_Price ($): "))
GST_Rate=0.08 # 8%


# Arithmetic Calculations
Subtotal = Product_Qty * Unit_Price 
GST = Subtotal * GST_Rate
Grand_Total= Subtotal + GST 


# Checking Eligibility By Logical Operations
high_total = Grand_Total>=100 
high_Qty = Product_Qty>=5
VIP_Eligibility = high_total or high_Qty


#Printing Desired Invoice
print("=" * 30)
print("      Invoice Reciept      ")
print("=" * 30)
print("Customer Name : ", Customer_name)
print("Customer ID : ", Customer_ID)
print("Counter No : ", Counter_No)
print("Product Name : ", Product_Name)
print("Product Qty : ", Product_Qty)
print("Unit Price ($) : ", Unit_Price)
print("-" * 30)
print("SubTotal : ",  Subtotal)
print("GST : ", GST)
print("Grand Total : ", Grand_Total)
print("-" * 30)
print("Is Qty>5 : ", high_Qty  )
print("Is Total>$100 : ", high_total)
print("VIP Discount Eligible : ", VIP_Eligibility)
print("=" * 30)