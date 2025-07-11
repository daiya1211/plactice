# -------------------------------------
# カバさんは$50.5を持っている。
# 友だち4人と食事をし、$27.5を支払い、
# 残った金額を5人で割って持ち帰ることにした。
# 現在のドル円相場を「105.3」と仮定し、
# 1人が持って帰る金額を「円単位」で表示させなさい。
# なお、正しく計算されている場合、
# 1人が持って帰る金額は484.38円となる。
# -------------------------------------

#現在のドル円相場を代入
str = '105.3'
print('現在のレートは',str,sep="")

# -------------------------------------
# 問1
# 入力してもらった数を数値に変換したい(小数にも対応)
# 以下に当てはまる選択肢はどれか。
# ア  str(str)
# イ  float(str)
# ウ  int(str)
# エ  len(str)

rate = float(str)

# -------------------------------------
# 問2
# 金額を支払い$を円にして5分割する計算を1行で行う
# 以下に当てはまる選択肢はどれか。
# ア  (50.5+27.5)+rate-5
# イ  50.5-27.5*rate/5
# ウ  (50.5-27.5)*rate/5
# エ  50.5*27.5*rate*5

yen = (50.5-27.5)*rate/5

# -------------------------------------
# 問3&問4
# 「1人が持って帰る金額は○○円です。」と1行で表示したい
# ※改行、スペースが入らないようにしたい。
# 以下に当てはまる選択肢はどれか。
# ア  len=""
# イ  int=""
# ウ  sep=""
# エ  tup=""
# オ  end=""
# カ  set=""
# キ  elif=""

print("1人が持って帰る金額は",end="")
print(yen,"円です。",sep="")
