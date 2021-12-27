from django import template

register = template.Library()

badwlist = ['fuck', 'cunt', 'shit']


@register.filter(name='Censor')
def Censor(value):
    if isinstance(value, str):
        for badw in badwlist:
            if badw in value:
                value = value.replace(badw, f'*censored*')
            else:
                continue
        return value

    else:
        raise ValueError(f'Невозможно цезурировать {type(value)}')
