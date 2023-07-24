from django import template

register = template.Library()

# Здесь определяем список нежелательных слов, которые нужно цензурировать
UNDESIRABLE_WORDS = ['хрен', 'хуесос', 'мудак']

@register.filter(name='censor')
def censor_text(value):
    for word in UNDESIRABLE_WORDS:
        value = value.replace(word, '***')
    return value