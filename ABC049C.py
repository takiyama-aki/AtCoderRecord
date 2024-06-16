s = input()[::-1]
ts = ["dream", "dreamer", "erase", "eraser"]
ts = [ts_i[::-1] for ts_i in ts]

# print(s)
# print(ts)
while len(s) > 0:
    flg = False
    for i in ts:
        if s.startswith(i):
            s = s[len(i):]
            #print("s:", s)
            flg = True
    if not flg:
        break
if len(s) == 0:
    print("YES")

else:
    print("NO")

