symbol = input("Введите букву: ")

original = ord(symbol)
new_code = (original  + 3) % 26 
new_symbol = chr(new_code)
print(f"{symbol} -> {new_symbol}")