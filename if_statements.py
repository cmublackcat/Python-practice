# if判斷句
# 一樣有內部縮排為四個空白or一個tab

# 1.
# 如果 我肚子餓
#     我就去吃飯
## 當False時，會繼續執行if外面的程式碼，由於在這裏if外面沒有其他的程式碼，所以程式碼不會有回應。
hungry=True
if hungry:
    print("我就去吃飯")

# 2.
# 如果 今天下雨
#     我就開車去上班
# 否則
#     我就走路去上班
rainy=False
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班")


# 3.
# 如果 妳考100分
#     我就給妳1000元
# 或是如果 妳考80分以上
#     我就給妳500元
# 或是如果 妳考60分以上
#     我就給妳100元
# 否則
#     妳給我300元

## ==判斷左右值是否相等，是的話為True
score=100
if score==100:
    print("我給妳1000元")
elif score>=80:
    print("我給妳500元")
elif score>=60:
    print("我給妳500元")
else:
    print("妳給我300元")

# 4.
# 如果 妳考100分 且 今天下雨
#     我給妳1000元
# 否則
#     妳給我100元
Score=100
rainy=True
if Score==100 and rainy:
    print("我給妳1000元")
else:
    print("妳給我100元")

# 5.
# 如果 妳考100分 或 今天下雨
#     我給妳1000元
# 否則
#     妳給我100元
SCore = 100
RAiny = True
if SCore==100 or RAiny:
    print("我給妳1000元")
else:
    print("妳給我100元")


# 6.
# 如果 妳考100分 或 沒有下雨
#     我給妳1000元
# 否則
#     妳給我100元
SCOre = 100
RAIny = False
if SCOre==100 or not (RAIny):
    print("我給妳1000元")
else:
    print("妳給我100元")

# 7.
# 如果 妳沒有考100分 或 沒有下雨
#     我給妳1000元
# 否則
#     妳給我100元
SCORe = 100
RAINY = True
if SCORe!=100 or not (RAINY):
    print("我給妳1000元")
else:
    print("妳給我100元")



# 練習:
# 今天要做一個函式max_num，這個函示要傳入三個參數，會回傳出最大的參數
def max_num():
    num1 = input("輸入第一個數字: ")
    num2 = input("輸入第二個數字: ")
    num3 = input("輸入第三個數字: ")
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num())

