from math import *

print("  /")
print(" / ")
print("/__")

# 註解不會被印出
print("隨便寫都不會有問題")
# 下面的程式碼印出貓貓的年齡
print("貓貓13歲")
# 字串，可以用單引號或雙引號
"貓貓"'卯咪'

# 數字
70
-87
160.3
180.5431

# 布林值 
True
False

# 變數，命名規則
# 1.明成只能是英文or數字or_的組和
# 2.變數的開頭不可以是數字

name = "blackcat"
age = 13
is_male = True

print("有隻貓叫" + name)
print(name + "今年13歲")
print(name + "長度30公分")
# replace()->置換，將前面的字元由後面的字元做置換
print(name.replace("b","B"))
# isupper()->確認是否都大寫，否則傳Flase
print(name.isupper())
# islower()->確認是否都小寫
print(name.islower())

# 如何使用數字、數字的用法
number = -6
# abs->取絕對值
print(abs(number))
# %->取餘數，number除以10後取餘數
print(number%10)
# str()->轉換括號中的型態為字串
print("標示為" + str(25))
# Max(), Min()->顯示數列的最大值，最小值
print(max(5,41,2884,643128))
print(min(2,874,26,77,45863))
# pow()->次方的意思，括號中要放兩個數字:前面放基數，後面為次方數
print(pow(2,10))
# round()->取四捨五入
print(round(3.2))
# floor() 無條件捨去
print(floor(5.1))
# ceil()->無條件進位
print(ceil(6.3))
# sqrt()->開根號 
print(sqrt(4))

# input預設會當字串來看
Name = input("請輸入你的名字: ")
age = input("請輸入你的年紀: ")
print("Hi"+ Name +"你今年" + age + "歲")
# 建立基本計算機(相加)
# int()->轉換字串為整數
# float()->轉換字串帶小數點的數
number1 = input("請輸入第一個數字: ")
number2 = input("請輸入第二個數字: ")
print(float(number1) + float(number2))

## 列表list、列表的用法
# 列表是可以放置很多值資料型態

Scores = [90,60,70,48,6]
friends = ["小貓","小狗","小魚" ] 
thing = [900, "小貓", True]
# 取列表中的資料
# [A]->取A值
# [A:B]->從A位開始取到B位之前，不包含B位
# [A:]->從A位開始取到最後所有值
# [:B]->取得B位之前的所有值，不包含B位
print(Scores[1:4])

# extend()->列表後面延伸
# append()->列表後面增加值
# insert(A,B)->插入，A位列表中的順序，B為插入值
# remove()->移除
# clear()->清空列表，括號中不需要放值
# pop()->移除列表最後一位，括號中不須放值
# sort()->由小到大排列列表，括號中不須放值
# reverse()->列表做反轉，括號中不須放值
# index(A)->尋找A是在列表中的第幾位
# count(A)->回傳列表中有幾個A
print(Scores.count(90))

# 元組 tuple
scores = (90,80,60,50,20)
print(len(scores))
# len()->元組內有多少值(在列表中一樣可以用)
# 元組跟列表的差別：元組創建之後，無法做修改(新增、刪除)

