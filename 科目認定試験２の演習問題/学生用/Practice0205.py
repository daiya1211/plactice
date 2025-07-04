
import math

def circle(radius):
  return math.floor(radius * radius * math.pi)

def cone(circle, height):
  return math.floor(circle * height)

try:
  radius = int(input('半径を入力：'))
  circle = circle(radius)
  print("半径が" + str(radius) + "の円の面積は" + str(circle) + "です。")
  height = int(input('高さを入力：'))
  cone = cone(circle, height)
  print("底面積が" + str(circle) + "で高さが" + str(height) + "の円柱の体積は" + str(cone) + "です。")

except ValueError:
  print('整数で入力をして下さい')