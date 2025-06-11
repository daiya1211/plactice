import random
def a():
    return random.randint(1,4)
print("本日の運勢：",end = "")
if a() == 1:
    print("絶好調")
elif a() == 2:
    print("好調")
elif a() == 3:
    print("不調")
else:
    print("絶不調")