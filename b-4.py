def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # 全国の平均気温
    total_temp = [info["temperature"] for info in weather_information]
    avg_temp = sum(total_temp) / len(total_temp)  # 合計 ÷ 件数
    print(avg_temp)

    # 大阪府の駅名（カンマ区切り）
    osaka_stations = [info["station"] for info in weather_information if info["prefecture"] == "大阪府"]
    print(','.join(osaka_stations))

    # 福岡県の平均気温
    fukuoka_temp = [info["temperature"] for info in weather_information if info["prefecture"] == "福岡県"]
    avg_fukuoka = sum(fukuoka_temp) / len(fukuoka_temp)
    print(avg_fukuoka)


if __name__ == "__main__":
    main()
