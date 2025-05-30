total = 0
count = 0

while True:
    n = int(input("整数を入力:"))
    if n == 0:
        break
    total += n
    count += 1

if count == 0:
    print("入力された整数はありません。")
else:
    average = total / count
    print(f"合計値: {total}")
    print(f"平均値: {average}")
