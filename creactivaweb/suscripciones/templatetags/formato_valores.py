from django import template

register = template.Library()

@register.filter
def separador_miles(valor):
    try:
        valor_str = str(valor)
        str_result = ""
        str_reversed = valor_str[::-1]
        for x, a in enumerate(str_reversed):
            if (x+2)%3 == 0:
                str_result += valor_str[x]
                str_result += "."
            else:
                str_result += valor_str[x]
        return str_result
    except (ValueError, TypeError):
        return valor