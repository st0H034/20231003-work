from math import ceil

"""タクシーの運賃計算
    タクシーの運賃を計算するコードを作成せよ
    * 初乗り運賃は 1700m までは610円とする
    * 1700mを超えるとその後は 315m毎に 80円増えるものとする
    * 引数として走行距離(整数でm単位)が渡されるものとする
    * 戻り値は金額(整数値)とする
    * 1mでも超えれば80円単位でかかるものとする
    * 0mおよびマイナスの場合はNoneを返す
"""
def calc_account(m):
    # 定数の定義
    INITIAL_RIDING_DISTANCE = 1700  # 初乗り距離
    INITIAL_FARE = 610  # 初乗り運賃
    MILEAGE = 315   #走行距離
    M_MONEY = 80    # 距離ごとにかかるお金

    if 0 < m and m <= INITIAL_RIDING_DISTANCE:    # 走行距離が初乗り距離以下だった場合
        return INITIAL_FARE
    elif INITIAL_RIDING_DISTANCE < m:   # 走行距離が初乗り距離より上だった場合
        m1 = m - INITIAL_RIDING_DISTANCE    # 1700以上の距離の算出
        if m1 <= MILEAGE:   # 315m以下だった場合
            return INITIAL_FARE + M_MONEY
        else:
            cnt = 0
            while MILEAGE < m1:
                cnt += 1
                m1 = m1 - MILEAGE
            if 1 <= m1:
                cnt += 1
            return INITIAL_FARE + M_MONEY * cnt
    elif m <= 0:    # 走行距離が0以下だった場合
        return None



if __name__ == "__main__":
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description="引数に金額を渡すとタクシー料金を計算します")
    parser.add_argument("distance", help="走行距離(メートル)", type=int)

    args = parser.parse_args()
    d = args.distance
    a = calc_account(d)
    if a == None:
        print("不正な数値です、1以上の整数値を渡してください", file=sys.stderr)
        sys.exit(1)
    print(f"走行距離 {args.distance}m => 金額は {calc_account(args.distance)}円です。")


