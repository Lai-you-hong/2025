print(True or False)
print(True and False)
print(not True)
'''''''''''''''''''''''''''''
a=5
b=3
print (a&b)
print (a|b)
print (a^b)
print (~a)
'''''''''''''''''''''''''''''
x = 1
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
'''''''''''''''''''''''''''''
age = int(input("請輸入年齡 "))

if age >= 18:
    if age == 20:
        print("您已成年，可以公民投票，也可以選舉罷免！")
    else:
        print("您已成年，可以公民投票！")
else:
    print("您未成年，無法投票。")
'''''''''''''''''''''''''''''
國 = int(input("國文成績: "))
數 = int(input("數學成績: "))
自 = int(input("自然成績: "))
英 = int(input("英文成績: "))
地 = int(input("地理成績: "))
歷 = int(input("歷史成績: "))
公 = int(input("公民成績: "))
總分 = 國 + 數 + 自 + 英 + 地 + 歷 + 公
平均 = 總分 / 7

print(f"國文: {國}")
print(f"數學: {數}")
print(f"自然: {自}")
print(f"英文: {英}")
print(f"地理: {地}")
print(f"歷史: {歷}")
print(f"公民: {公}")

print(f"總分: {總分}")
print(f"平均: {平均:.2f}")
