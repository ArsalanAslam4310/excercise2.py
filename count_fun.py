def count(string):
    chars=0
    digit=0
    symbol=0

    for char in string:
        if char.isalpha():
            chars = +1
        elif char.isdigit():
            digit = +1
        else:
            symbol = +1
    print("Chars =", chars, "Digits =", digit, "Symbol =", symbol)


string ="ckjfcn543&*(^%52"
x = count(string)
print(x)


