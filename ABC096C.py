height, width = map(int, input().split())

canvas = [list(input()) for _ in range(height)]

# 黒色の上下左右が白色の絵は描けない

# 1マスずつ見ていく
for y in range(height):
    for x in range(width):
        # 見てるマスが黒色だったら
        if canvas[y][x] == "#":
            count = 0

            # 上下左右のマスを見ていく
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if dx == 0 and dy == 0:
                        continue
                    if dx == 1 and dy == 1:
                        continue
                    if dx == -1 and dy == -1:
                        continue

                    # 左右
                    xx = x + dx
                    # 上下
                    yy = y + dy

                    if xx >= 0 and xx < width and yy >= 0 and yy < height:
                        #print("yy = y",dy,"[",canvas[yy][xx], "], xx = x",dx, "[", canvas[yy][xx],"]")
                        if canvas[yy][xx] == "#" or canvas[yy][xx] == "#":
                            #print("good")
                            # この黒マスはok
                            count += 1
                    
            if count == 0:
                #print(y, x)
                print("No")
                exit()

print("Yes")


