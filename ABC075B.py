# グリッドに関する問題

height, width = map(int, input().split())
field = [list(input()) for _ in range(height)]

for y in range(height):
    for x in range(width):
        # y行x列の文字が「.」だったら
        if field[y][x] == ".":
            count = 0
            # 前後上下を調べる
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if dx == 0 and dy == 0:
                        continue
                    # 今見てる座標の前後上下の座標を取得する
                    xx = x + dx
                    yy = y + dy

                    # 端っこかどうか確認
                    if xx >= 0 and xx < width and yy >= 0 and yy < height:
                        if field[yy][xx] == "#":
                            count += 1
            field[y][x] = count

for y in range(height):
    ans = ''.join(map(str, field[y]))
    print(ans)