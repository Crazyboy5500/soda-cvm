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
