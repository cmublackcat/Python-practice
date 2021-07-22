# 函式 function->預先寫好的程式碼，做資料的運算
# 分成兩部分，定義(命名與變數的規則相同)與呼叫
# 函式的內部縮排為四個空白or一個tab
## 練習，定義一個函式：傳入兩個數字，函式會輸出兩個數字的相加
def Add():
    number_1 = input("輸入第一筆數字: ")
    number_2 = input("輸入第二筆數字: ")
    result = (float(number_1) + float(number_2))
    print(result)

Add()

# 解答 from https://www.youtube.com/watch?v=zdMUJJKFdsU&t=5355s
def add(num1,num2):
    print(num1+num2)
add(2,3)

# 函式回傳
# return->程式碼碰到return會覆蓋掉原先的呼叫，不會再執行之後的程式碼。
def add(num1,num2):
    # print(num1+num2)
    return num1+num2

print(add(2,3))



# 考題，當按下執行後，下列程式碼會印出什麼東西？
# 由於return會覆蓋下面的呼叫，所以我認為會顯示10
## 解答：會顯示出7 10。
### 程式碼會先運行函式print(num_1 + num_2)，之後碰到return 10 (覆蓋掉value)。所以最後出的結果是7 10。
def add(num_1, num_2):
    print(num_1 + num_2)
    return 10

value = add(3,4)
print(value)

# 函式中會預設return None，當下方程式碼執行後，會呈現7 None的結果。
def add(num_1, num_2):
    print(num_1 + num_2)


value = add(3,4)
print(value)
