# for 迴圈
# 常搭配”range"使用




# for 變數 in 字串or列表：
#     要重複執行的程式碼

# for letter in "喵喵":
#     print(letter)

# for num in [0, 1, 2, 3, 4, 5]:
#     print(num)

# for num in range(2,7)
#     print(num)

# 做一個函式，實現x的y次方
count = int (2*2*2*2*2*2)
for num in count:
    print (num)

# 做一個函式，實現x的y次方  解答篇
def power(base_num, pow_num):
    result = base_num
    for index in range(pow_num-1):
        result = result * base_num
    return result
print(power(2,5))
