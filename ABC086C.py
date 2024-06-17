# マンハッタン距離
# まだ理解できてない

n = int(input())
can = False

plans = []
for _ in range(n):
    plans.append(map(int, input().split()))

st, sx, sy = 0, 0, 0

for t, x, y in plans:
    # 時間tの差
    dt = t - st
    
    # xの移動の絶対値
    dx = abs(x - sx)

    # yの移動の絶対値
    dy = abs(y - sy)

    # 偶数秒
    if t%2 != (x+y)%2 or dx + dy > dt:
        print("No")
        exit()
    st, sx, sy = t, x, y
print("Yes")