import re
from collections import Counter

def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())

def words_in_parentheses(text):
    return re.findall(r'\((.*?)\)', text)

def is_valid_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

def unique_characters(text):
    result = ""
    for ch in text:
        if ch not in result:
            result += ch
    return result

def is_palindrome(text):
    clean = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return clean == clean[::-1]

def most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word, count = Counter(words).most_common(1)[0]
    return word, count

def format_string(text):
    return "-".join(text[i:i+3] for i in range(0, len(text), 3))
