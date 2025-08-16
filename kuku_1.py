# 九九表を出力（数字の後ろに半角スペース）

for i in range(1, 10):
    line = ""
    for j in range(1, 10):
        line += f"{i * j} "
    print(line)
