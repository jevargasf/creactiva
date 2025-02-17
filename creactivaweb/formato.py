def separador_miles(valor):
    try:
        valor_str = str(valor)
        str_result = ""
        str_reversed = valor_str[::-1]
        for x, a in enumerate(str_reversed):
            if (x+2)%3 == 0:
                print(a)
                str_result += str_reversed[x]
                str_result += "."
            else:
                str_result += str_reversed[x]
        return str_result
    except (ValueError, TypeError):
        return valor
    
print(separador_miles(12000))
print(separador_miles(8333))