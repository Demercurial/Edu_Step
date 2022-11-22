def is_correct_bracket(text):
    k = 0
    for c in text:
            if c == '(':
                k += 1
            else:
                k -= 1
                if k < 0:
                    break
    if k == 0:
        return True
    else:
        return False

txt = list(input())
print(is_correct_bracket(txt))