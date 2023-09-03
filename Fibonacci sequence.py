choose = int(input(" enter number :"))
x = 0
y = 1
i = 0
m = [0, 1]

if choose > 1:
    while i < choose:
        t = x + y
        x = y
        y = t
        m.append(t)
        l = m
        i += 1
elif choose == 0:
    print("0")
elif choose == 1:
    print("[0,1]")

else:
    print(" most be positve namber")
print(m)
