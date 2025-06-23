with open("16_4_write.txt", "w", encoding="utf-8") as f:
    while True:
        s = input("入力: ")
        if s == "end":
            print("書き込み終了")
            break
        f.write(s + "\n")

