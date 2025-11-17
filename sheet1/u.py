n = input().strip()

# If number contains a decimal part
if "." in n:
    integer, decimal = n.split(".")

    # If decimal part is all zeros → treat as integer
    if int(decimal) == 0:
        print("int", integer)
    else:
        print("float", integer, "." + decimal)
else:
    # Pure integer input
    print("int", n)
