# 建立一個計算機
num_1 = float(input("請輸入第一個數："))
op = input("請輸入計算符號：")
num_２ = float(input("請輸入第二個數："))

if op=="+":
    print(num_1+num_2)
elif op== "-":
    print(num_1-num_2)
elif op== "*":
    print(num_1*num_2)
elif op=="/":
    print(num_1/num_2)
else:
    print("不支援的運算")
