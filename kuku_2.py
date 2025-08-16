# 入力された行数と列数で掛け算表を出力

rows = int(input("行数を入力してください: "))
cols = int(input("列数を入力してください: "))

for i in range(1, rows + 1):
    line = ""
    for j in range(1, cols + 1):
        line += f"{i * j} "
    print(line)
