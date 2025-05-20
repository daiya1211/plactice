print("税込価格を求めます")


price = int(input("定価:"))
tax_rate = int(input("消費税率:"))


tax_included_price = price + (price * tax_rate // 100)


print(f"定価 = {price}")
print(f"税率 = {tax_rate}")
print(f"税込価格 = {tax_included_price}")

