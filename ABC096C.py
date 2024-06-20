height, width = map(int, input().split())

canvas = [list(input()) for _ in range(height)]

# 黒色の上下左右が白色の絵は描けない

for y in range(height):
    for x in range(width):
        if canvas[y][x] == "#":
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if dx == 0 and dy == 0:
                        continue

                    # 左右
                    xx = x + dx
                    # 上下
                    yy = y + dy

                    if xx >= 0 and xx < width and yy >= 0 and yy < height:
                        if xx == "#" or yy == "#":
                            # この黒マスはokだから次の黒マスへ
