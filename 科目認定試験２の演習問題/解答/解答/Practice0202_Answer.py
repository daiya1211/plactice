#######################################################
# 1～10までの整数の乱数を生成し、その乱数を1辺とする
# 正方形の面積を求める未完成プログラムがある。
# コメントを参考に空欄を埋めて、プログラムを完成させなさい。
#######################################################

#randomモジュールのインポート
#__(1)__ as rd
# ------------------------------------
# 問１以下に当てはまる選択肢はどれか
# 1. from random
# 2. import Random
# 3. import random
# ------------------------------------
# 回答
import random as rd


#randomモジュールの関数を用いて1~10の間の整数の乱数を生成する
#rd_num = rd.__(2)__(1,10)
# ------------------------------------
# 問２以下に当てはまる選択肢はどれか
# 1. random
# 2. randint
# 3. randorange
# ------------------------------------
# 回答
rd_num = rd.randint(1,10)


#乱数の表示
print("生成した乱数は",rd_num,"です。")
#関数を呼び出し、正方形の面積を表示
#print("１辺が",rd_num,"の正方形の面積は",__(3)__,"です。")
# ------------------------------------
# 問３以下に当てはまる選択肢はどれか
# 1. rd_num*rd_num*3.14
# 2. rd_num*2
# 3. rd_num*rd_num
# ------------------------------------
# 回答
print("１辺が",rd_num,"の正方形の面積は",rd_num*rd_num,"です。")
