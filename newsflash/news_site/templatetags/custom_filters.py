from django import template
import re

register = template.Library()

@register.filter
def truncate_words_at(text, length):
    words = text.split()
    if len(words) > length:
        truncated_text = ' '.join(words[:length]) + '...'
        return truncated_text
    return text
