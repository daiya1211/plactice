
copy_from = input("コピー元ファイル名: ")
copy_to = input("コピー先ファイル名: ")

with open(copy_from, "r", encoding="utf-8") as f_read:
    data = f_read.read()

with open(copy_to, "w", encoding="utf-8") as f_write:
    f_write.write(data)

print(f"\n[{copy_from}]")
print(data)

print(f"\n[{copy_to}]")
with open(copy_to, "r", encoding="utf-8") as f_check:
    print(f_check.read())
