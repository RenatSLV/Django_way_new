from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='remove_vowels')
def remove_vowels(value):
    vowels = 'аеёиоуыэюяaeiou'
    return ''.join(char for char in value if char.lower() not in vowels)


@register.filter(name='repeat')
def repeat(value, times):
    try:
        return str(value) * int(times)
    except:
        return value


@register.simple_tag
def current_time(format_string="%H:%M:%S"):
    return datetime.now().strftime(format_string)


# Тег 2: Считает количество слов в строке
@register.simple_tag
def word_count(text):
    return len(text.split())
