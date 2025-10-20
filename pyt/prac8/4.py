def convert_base(number, from_base, to_base):
    try:
        decimal_num = int(number, from_base)
        
        if to_base == 10:
            return str(decimal_num)
        
        result = ""
        
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        n = decimal_num
        while n > 0:
            remainder = n % to_base
            result = digits[remainder] + result
            n //= to_base
        
        return result if result else "0"
        
    except ValueError:
        return "Ошибка: некорректное число или система счисления"

if __name__ == "__main__":
    print("=== Конвертер систем счисления ===\n")
    
    print("255 (10 → 16):", convert_base("255", 10, 16))
    
    print("1010 (2 → 10):", convert_base("1010", 2, 10))
    
    print("10 (10 → 2):", convert_base("10", 10, 2))
    
    print("FF (16 → 10):", convert_base("FF", 16, 10))
    
    print("\nТест с ошибкой (некорректное число):")
    print(convert_base("XYZ", 10, 2))