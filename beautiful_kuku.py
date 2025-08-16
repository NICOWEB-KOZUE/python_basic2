# 行数と列数を指定して「1 x 1 = 1」形式で掛け算表を出力

rows = int(input("行数を入力してください: "))
cols = int(input("列数を入力してください: "))

# 掛け算表を作成
for i in range(1, rows + 1):
    line = ""
    for j in range(1, cols + 1):
        line += f"{j} x {i} = {i * j:2} | "
    print(line)
