bills, money = map(int, input().split())
flg = False

manA = -1
gosenA = -1
senA = -1
for man in range(bills+1):
    for gosen in range(bills+1-man):
        sen = bills - man - gosen
        if sen < 0:
            continue

        total = 10000*man + 5000*gosen + 1000*sen

        if total == money:
            manA = man
            gosenA = gosen
            senA = sen
            break

    if flg:
        break

print(manA, gosenA, senA)