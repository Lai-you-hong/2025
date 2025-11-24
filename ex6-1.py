a = int(input("請輸入直角三角形邊長a "))
b = int(input("請輸入直角三角形邊長b "))
print(f"斜邊長: {(a*a + b*b)**0.5:.2f}")
''''''''''''''''''''''''''''''''''''''''''''''''''''''
a = int(input("請輸入直角三角形邊長a "))
b = int(input("請輸入直角三角形邊長b "))
print(f"斜邊長: {(a*a + b*b)**0.5:.2f}")
''''''''''''''''''''''''''''''''''''''''''''''''''''''
r = float(input("請輸入圓的半徑： "))

if r >= 0:
    a = 3.14159 * r * r
    a = 2 * 3.14159 * r
    print(f"圓面積 = {a:.2f}")
    print(f"圓周長 = {b:.2f}")
else:
    print("半徑不能是負數")

''''''''''''''''''''''''''''''''''''''''''''''''''''''
print(2.1234344566e23)
''''''''''''''''''''''''''''''''''''''''''''''''''''''
username = "qwertyuiop"
password = "123456"
is_active = True

if username == "qwertyuiop" and password == "123456" and is_active:
    print("登入成功！")
elif not is_active:
    print("帳號已被停用")
else:
    print("使用者名稱或密碼錯誤")
''''''''''''''''''''''''''''''''''''''''''''''''''''''
a = float(input("請輸入邊長 a: "))
b = float(input("請輸入邊長 b: "))

c = (a*a + b*b) ** 0.5

print(f"情況一（a、b 為兩股）→ 斜邊 c = {c:.2f}")

if a > b and a*a - b*b >= 0:
    c = (a*a - b*b) ** 0.5
    print(f"情況二（a 為斜邊）→ 另一股 c = {c:.2f}")
else:
    c = (b*b - a*a) ** 0.5
    print(f"情況二（b 為斜邊）→ 另一股 c = {c:.2f}")
''''''''''''''''''''''''''''''''''''''''''''''''''''''
year = int(input("請輸入西元年份： "))
month = int(input("請輸入月份（1-12）： "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("這個月有 31 天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("這個月有 30 天")
elif month == 2:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("這個月有 29 天（閏年）")
    else:
        print("這個月有 28 天")
else:
    print("月份不正確！")
''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = float(input("請輸入第一個數： "))
y = float(input("請輸入第二個數： "))

if x > y:
    print(f"最大值 = {x}")
elif y > x:
    print(f"最大值 = {y}")
else:
    print("兩個數一樣大！")
