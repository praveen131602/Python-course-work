units = int(input("Enter the units: "))

bill = 0
tax_amount = 0
final_amount = 0

# Calculate bill based on units
if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

# Discount if bill is large
if final_bill >= 5000:
    final_bill -= 500

# Tax calculation (5%)
tax_amount = bill * 0.05

# Final amount
final_amount = bill + tax_amount

print(f"Units Consumed : {units}")
print(f"Total Bill Before Tax : {bill}")
print(f"Tax Amount : {tax_amount}")
print(f"Final Payable Amount : {final_amount}")
