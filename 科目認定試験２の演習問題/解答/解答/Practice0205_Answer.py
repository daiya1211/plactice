############################################################################
# 半径の値を引数で受け取り、円の面積を小数点切り捨てで戻す関数を作成。
# 円の面積「半径×半径×円周率」
# 底面積と高さを引数で受け取り、円すいの体積を出す関数を作成。
# 円すいの体積は「底面積×高さ×1/3」
# コメントを参考に空欄を埋めて、プログラムを完成させなさい。
############################################################################

# mathモジュールのインポート
#import __(1)__
# -------------------------------------
# 問１以下に当てはまる選択肢はどれか
# 1. mathematics
# 2. arithmetic
# 3. math
# -------------------------------------
### 答え
import math

# 関数circle(円の面積)の定義
 #引数 radius(半径) 戻り値 circle(円の面積)
def circle(radius):
  #return math.floor(__(2)__)
  # -------------------------------------
  # 問２以下に当てはまる選択肢はどれか
  # 1. radius ** 2 * pi
  # 2. 2 * radius * math.pi
  # 3. radius * radius * math.pi
  # -------------------------------------
  ### 答え
  return math.floor(radius * radius * math.pi)
 
# 関数cone(円錐の体積)の定義
def cone(circle, height):
  #return math.floor(__(3)__)
  # -------------------------------------
  # 問２以下に当てはまる選択肢はどれか
  # 1. circle / height
  # 2. circle * height * 1/3
  # 3. circle * circle * pi * height * 1/3
  # -------------------------------------
  ### 答え
  return math.floor(circle * height * 1/3)

# 正数以外の入力は実行時エラー
try:
  # 入力の受付と、関数の呼び出し、出力
  radius = int(input('半径入力:'))
  circle = circle(radius)
  print('円の面積は{}'.format(circle))
  height = int(input('高さ入力：'))
  cone = cone(circle, height)
  print('円錐の体積は{}'.format(cone))

except ValueError:
  print('整数で入力をして下さい')