def order():
    global o
    for i in range(o, x + 1):
        y = int(input(f"Enter The ID of drink {i}: "))
        if 0 > y or y > 7:
            print("Invalid Product Id Enter it again")
            o = i
            order()
            receipt()
            conf()
            break
        else:
            order_index.append(y)

def receipt():
    total = 0
    print("\n")
    print("          Receipt")
    print("----------------------------")
    for i in order_index:
        print(f"     {drinks[i]}-----{price[i]}")
        total += price[i]
        print()
    print(f"     Your total is: {total}")


def conf():
    global x
    global o
    confirmation = input("""\nDo you want to confirm your purchase?\nEnter "y" to confirm,"a" to add, "e" to replace, 
    "r" to remove.\n-->""")
    if confirmation == "a" or confirmation == "A":
        o = x + 1
        x = x + 1
        order()
        receipt()
        conf()
    elif confirmation == "y" or confirmation == "Y" or confirmation == "":
        print("Order confirmed!!\nPay to get your drinks.\nThanks for buying from us.\nVisit again.")
        exit()
    elif confirmation == "e" or confirmation == "E":
        rep = int(input("which drink do you want to replace?\n-->"))
        repment = int(input("Enter the id of the drink you want to replace the old one with.\n-->"))
        order_index[rep-1] = repment
        receipt()
        conf()
    elif confirmation == "r" or confirmation == "R":
        rem = int(input("Enter the drink you want to remove.\n-->"))
        order_index.remove(order_index[rem-1])
        x = x - 1
        receipt()
        conf()
    else:
        print("Invalid input.")
        conf()
