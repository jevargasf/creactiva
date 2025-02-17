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
        return str_result[::-1]
    except (ValueError, TypeError):
        return valor