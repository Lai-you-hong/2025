a = float(input("請輸入第 1 個數: "))
b = float(input("請輸入第 2 個數: "))
c = float(input("請輸入第 3 個數: "))

avg = (a + b + c) / 3
print("平均值 =", avg)
''''''''''''''''''''''''''''''''''''''''
print("印出 0 到 4：")
for i in range(5):
    print(i)

print("\n印出 1 到 10：")
for i in range(1, 11):
    print(i, end=" ")
print("\n\n印出 2 到 20 的偶數：")
for i in range(2, 21, 2):
    print(i, end=" ")
''''''''''''''''''''''''''''''''''''''''
while True:
    print("\n=== 簡單計算機 ===")
    print("1. 加法")
    print("2. 減法")
    print("3. 退出")
    
    choice = input("請選擇功能（1-3）：")
    
    if choice == "3":
        print("謝謝使用，再見！")
        break
    elif choice == "1":
        a = float(input("請輸入第一個數字："))
        b = float(input("請輸入第二個數字："))
        print(f"結果：{a} + {b} = {a + b}")
    elif choice == "2":
        a = float(input("請輸入第一個數字："))
        b = float(input("請輸入第二個數字："))
        print(f"結果：{a} - {b} = {a - b}")
    else:
        print("無效的選擇，請重新選擇。")
''''''''''''''''''''''''''''''''''''''''
def get_day_message(day):
    match day:
        case "星期一":
            return "新的一週開始！加油！"
        case "星期二":
            return "繼續努力，還有四天！"
        case "星期三":
            return "週中了，堅持下去！"
        case "星期四":
            return "快到週末了！"
        case "星期五":
            return "TGIF！明天就是週末！"
        case "星期六" | "星期日":  
            return "享受週末時光！"
        case _:
            return "請輸入有效的星期"

day = input("輸入今天星期幾：")
print(f"{day}: {get_day_message(day)}")
''''''''''''''''''''''''''''''''''''''''
def get_grade_comment(score):
    match score:
        case n if 90 <= n <= 100:
            return "優秀！"
        case n if 80 <= n < 90:
            return "良好！"
        case n if 70 <= n < 80:
            return "普通"
        case n if 60 <= n < 70:
            return "需要加油"
        case n if 0 <= n < 60:
            return "不及格，需要重修"
        case _:
            return "無效分數"

scores = [int(s) for s in input().split()]

for s in scores:
    print(f"分數 {s}: {get_grade_comment(s)}")
''''''''''''''''''''''''''''''''''''''''
a = int(input("輸入第一個整數: "))
b = int(input("輸入第二個整數: "))
c = int(input("輸入第三個整數: "))
d = int(input("輸入第四個整數: "))

m = min(a, b, c, d)
print("最小的數是:", m)
''''''''''''''''''''''''''''''''''''''''
x = float(input("輸入第一個數: "))
y = float(input("輸入第二個數: "))

m = max(x, y)
print("最大值是:", m)
''''''''''''''''''''''''''''''''''''''''
p = 0
n = 0
z = 0

for i in range(10):
    a = int(input("輸入整數: "))
    if a > 0:
        p += 1
    elif a < 0:
        n += 1
    else:
        z += 1

print("正數個數:", p)
print("負數個數:", n)
print("零的個數:", z)
