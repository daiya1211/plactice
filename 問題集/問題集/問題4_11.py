#a = int(input())

'''
if a%400 == 0:
    print("閏年")
elif a%100 == 0:
    print("平成")
elif a%4 == 0:
    print("閏年")
else:
    print("平成")
'''
eyer = int(input())
if eyer % 4 == 0 and eyer % 100 != 0 or eyer % 400 == 0:
    print("閏年です")
else:
    print("平年です")