zip_code = input("What is your zipcode? ")
if len(zip_code) != 5:
    print("You have entered an incorrect zipcode, cya!")
else:
    if zip_code[0] == "6" and zip_code[1] == "0":
        print("You live in the greater Chicago area.")
    else:
        print("I do not know where you live mate.")
