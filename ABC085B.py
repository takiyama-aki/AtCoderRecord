mochi_n = int(input())
mochis = []
before_mochi = 101
ans = 0

for mochi_i in range(mochi_n):
    mochis.append(int(input()))

# もちリストを大きい順にソート
mochis.sort(reverse=True)

for mochi_i in mochis:
    if mochi_i < before_mochi:
        ans += 1
        before_mochi = mochi_i
    else:
        before_mochi = mochi_i
        continue

print(ans)