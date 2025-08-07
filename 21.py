#if applicant has high income AND
#good credit. Eligible foe loan

has_high_income = False
has_good_credit = False

if has_high_income or has_good_credit:
    print ("Eligible for loan")

else:
    print("not eligible for loan")


#another example

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print ("Eligible for loan")

else:
    print("not eligible for loan.")
