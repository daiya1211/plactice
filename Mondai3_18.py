print("税込価格を求めます")


a = int(input("定価:"))
b = int(input("消費税率:"))


c = a + (a * b // 100)


print(f"定価 = {a}")
print(f"税率 = {b}")
print(f"税込価格 = {c}")

