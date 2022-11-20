def is_password_good(password):
    flag1, flag2, flag3, flag4 = False, False, False, False
    if len(password) >= 8:
        flag4 = True
        for i in password:
            if i.isdigit():
                flag1 = True
            elif i.islower():
                flag2 = True
            elif i.isupper():
                flag3 = True

    return flag1 and flag2 and flag3 and flag4


txt = list(input())  # Ввод пароля
print(is_password_good(txt))
