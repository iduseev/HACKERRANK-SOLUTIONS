def birthdayCakeCandles(candles):
    tallest_candles = []
    max_candle = max(candles)
    for candle in candles:
        if candle == max_candle:
            tallest_candles.append(candle)
    # print(tallest_candles)
    return len(tallest_candles)

if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

