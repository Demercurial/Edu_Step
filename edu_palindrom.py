from math import floor

def is_palindrome(text):
    text_low = ''.join(c.lower() for c in text if c.isalpha())
    text_obr = text_low[::-1][:floor(len(text_low)//2)]
    if text_low.startswith(text_obr):
        return True
    else:
        return False

txt = input()
print(is_palindrome(txt))