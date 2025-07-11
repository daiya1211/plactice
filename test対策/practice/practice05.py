# ------------------------------------------------------------------
# 複数の学生の得点を入力し、80点以上なら合格、その合格者数を表示する。
# また「exit」が入力されるまで得点を入力する。
# 数値と「exit」以外の値が入力された場合の処理は考慮しなくてよい。
# ------------------------------------------------------------------

# 値を格納するリストを用意する
lst = []
# 人数を表示するカウント変数
cnt = 1


# -----------------------------------------------------
# 問１__(1)__に当てはまる選択肢はどれか
# 1. for
# 2. while
# 3. if
# -----------------------------------------------------

# 得点の入力を行う無限ループ
__(1)__(True):
    # 入力の受付
    print(f'{cnt}人目の得点:', end='')
    val = input()

    # 値を調べて「exit」なら終了
    if val == 'exit':

# ------------------------------------------------
# 問２__(2)__に当てはまる選択肢はどれか
#  1. continue
#  2. break
#  3. go
# ------------------------------------------------
        __(2)__

    # カウント変数のインクリメント
    cnt += 1

# ---------------------------------------------------
# 問３ __(3)__に当てはまる選択肢はどれか
#  1. append
#  2. add
#  3. addition
# ---------------------------------------------------
    # リストに値を追加
    lst.__(3)__(val)

# 合格人数を格納する変数
pass_check = 0
for score in lst:
    # 80以上ならカウント変数を増やす
    if 80 <= int(score):
        pass_check += 1

# 全体の数と合格者数の数を出力する
print(f'合格者数は{len(lst)}人中{pass_check}人')
