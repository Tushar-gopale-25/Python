pin = 1234
cb = 5000

for i in range(3):
    p = int(input("Enter pin: "))
    if p == pin:
        print("Pin is correct")
        wb = int(input("Enter amount to withdraw: "))
        if cb >= wb:
            cb = cb - wb
            print("Transaction successful")
            print("Your current balance is:", cb)
        else:
            print("Insufficient balance")
            print("Transaction unsuccessful")
        break  
    else:
        print("Pin is incorrect")
else:
    print("Card blocked")