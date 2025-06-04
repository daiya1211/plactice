
lst = []
cnt = 1
while(True):
    print(f'{cnt}人目の得点:', end='')
    val = input()
    if val == 'end':
        break
    cnt += 1
    lst.append(val)
pass_check = 0
for score in lst:
    if 60 <= int(score):
        pass_check += 1
print(f'合格者数は{len(lst)}人中{pass_check}人')