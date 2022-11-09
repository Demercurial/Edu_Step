# put your python code here
num_1, num_2 = int(input()), int(input())
con = 0
for i in range(num_1, num_2 + 1):
    for j in range(2, i + 1):
        if i % j == 0:
            con += 1
    if con == 1:
        print(i)
    con = 0
