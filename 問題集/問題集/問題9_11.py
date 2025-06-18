import random
def a():
    return random.randint(1,4)

# 運勢の値を一度だけ取得
result = a()
print("本日の運勢：",end = "")
if result == 1:
    print("絶好調".ljust(10))
elif result == 2:
    print("好調".ljust(10))
elif result == 3:
    print("不調".ljust(10))
else:
    print("絶不調".ljust(10))