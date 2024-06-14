# ABC088B - Card Game for Two

card_num = int(input())
card_list = sorted(map(int, input().split()), reverse=True)

alicePoint = 0
bobPoint = 0
flg = True # True: alice's turn, False: bob's turn

for i in range(card_num):
    if flg:
        alicePoint += card_list.pop(0)
        flg = False
    else:
        bobPoint += card_list.pop(0)
        flg = True

print(alicePoint-bobPoint)