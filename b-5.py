# 合計値を求める関数
def calc_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


# 最大値を求める関数
def calc_max(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value


# 最小値を求める関数
def calc_min(numbers):
    min_value = numbers[0]
    for n in numbers:
        if n < min_value:
            min_value = n
    return min_value


# 平均値を求める関数
def calc_avg(numbers):
    total = calc_total(numbers)
    return total // len(numbers)


# メイン処理
def main():
    input_date = input("データを入力してください(スペース区切り) > ")
    numbers = [int(x) for x in input_date.split()]

    print("合計値:", calc_total(numbers))
    print("最大値:", calc_max(numbers))
    print("最小値:", calc_min(numbers))
    print("平均値:", calc_avg(numbers))


if __name__ == "__main__":
    main()
