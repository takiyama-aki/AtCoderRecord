n = int(input())
s = list(input().split())
ans = 0
for a_i in range(2*n):
    tmpColor = s[a_i]
    count = 0
    flg = False
    
    for a_j in range(a_i+1,2*n):
        #print("["+str(a_i+1)+"]","a_i =",s[a_i],"a_j =",s[a_j])
        if s[a_j] != tmpColor:
            count += 1
        if s[a_j] == tmpColor:
            flg = True
            break

    if count == 1 and flg:
        #print("a_i is",s[a_i])
        ans += 1

print(ans)