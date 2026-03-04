salary = int(input("enter your salary :"))
credit_score =int(input("enter your Credit score :"))
existing_loan = int(input("Loan :"))
if salary > 30000 and credit_score > 700 and existing_loan < 50000:
                    print("eligible")
else:
    print("not eligible")
                    
