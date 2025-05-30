#0 == "グー"
#1 == "チョキ"
#2 == "パー"
import random
janken = ["グー","チョキ","パー"]
z = random.choice(janken)
#a = input("あなたの手を入力してください")
#print("あなたは" + a + "を出した！")
while print("your winner:(") or print("your loser:)"):
    a = input("あなたの手を入力してください")
    print("あなたは" + a + "を出した！")
#0 <= a <= 2
#random.randint(0,2
#janken = ["グー","チョキ","パー"]
#random.shuffle(janken)
#z = random.choice(janken)


    if  a == "グー" or "ぐー":
    #print("あなたは" + a + "を出した！")
    #random.shuffle(janken)
        print("相手は" + z + "を出した！")
        if z == "チョキ":
            print("your winner:(")
        elif z == "グー":
            print("あいこです")
        else:
            print("your loser:)")
        
    elif  a == "チョキ" or "ちょき":
    #print("あなたは" + a + "を出した！")
    #random.shuffle(janken)
        print("相手は" + z  + "を出した！")
        if z == "パー":
            print("your winner:(")
        elif z == "チョキ":
            print("あいこです")
        else:
            print("your loser:)")

    elif  a == "ぱー" or "パー":
    #print("あなたは" + a + "を出した！")
    #random.shuffle(janken)
        print("相手は" + z + "を出した！")
        if z == "グー":
            print("your winner:(")
        elif z == "パー":
            print("あいこです")
        else:
            print("your loser:)")
    
    