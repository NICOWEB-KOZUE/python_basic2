import random


def main():
    n = int(input("サイコロの面の数は？: "))

    m = int(input("何回振りますか?: "))

    results = [random.randint(1, n) for _ in range(m)]
    print(results)


if __name__ == "__main__":
    main()
