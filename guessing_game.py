# 猜數字遊戲
# 玩家輸入數字，電腦判斷數字是否大於或小於預設的數字，過大過小都會有對應的提示，次數無限制，猜到數字後會顯示"Win"

# target=23
# num = float (input("輸入一個數字")

# while num == target:
#     input("輸入一個數字")


# print("Win")



# 玩家輸入數字，電腦判斷數字是否大於或小於預設的數字，過大過小都會有對應的提示，次數無限制，猜到數字後會顯示"Win" 解答版

secret_num = 77
guess = None

while secret_num != guess:
    guess = int (input("請輸入數字"))
    if guess > secret_num:
        print("小一點")
    elif guess < secret_num:
        print("大一點")
    
print("Win")

# 增加限制，只能猜三次，超過也算玩家輸

secret_num = 77
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False

while secret_num != guess and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess = int (input("請輸入數字"))
        if guess > secret_num:
            print("小一點")
        elif guess < secret_num:
            print("大一點")
    else:
        out_of_limit = True
if out_of_limit:
    print("lose")
else:
    print("Win")
