class Calculator:
    def power(self, x, y):
        return x ** y

x = int(input("xを整数値で入力: "))
y = int(input("yを整数値で入力: "))

calc = Calculator()
result = calc.power(x, y)
print(f"{x}の{y}乗は{result}です。")
