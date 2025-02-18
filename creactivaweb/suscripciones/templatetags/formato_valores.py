from django import template

register = template.Library()

@register.filter
def separador_miles(valor):
    try:
        valor_str = str(valor)
        str_result = ""
        str_reversed = valor_str[::-1]
        for x, a in enumerate(str_reversed):
            if (x+4)%3 == 0:
                str_result += a
                str_result += "."
            else:
                str_result += a
        str_final = str_result[::-1]
        if str_final[0] == ".":
            return str_final[1:len(str_final)]
        else:
            return str_final
    except (ValueError, TypeError):
        return valor