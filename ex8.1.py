def greet():
    print("你好！歡迎學習Python！")
greet()
'''''''''''''''''''''''''''''''''''''''''''''
def greet(name):
    print(f"你好{name}！歡迎學習Python！")
greet("a")
greet("b")
'''''''''''''''''''''''''''''''''''''''''''''
def add_numbers(a, b):
    result = a + b
    return result
sum_result = add_numbers(67, 41)
print(f"67 + 41 = {sum_result}")
'''''''''''''''''''''''''''''''''''''''''''''
def add_numbers():
    a = float(input("請輸入第一個數字："))
    b = float(input("請輸入第二個數字："))
    return a + b

result = add_numbers()
print(f"結果是：{result}")
'''''''''''''''''''''''''''''''''''''''''''''
def circle(r):
    if r >= 0:
        area = 3.14159 * r * r
        length = 2 * 3.14159 * r
        print(f"圓的面積：{area}")
        print(f"圓的周長：{length}")
    else:
        print("半徑不能是負的！")

r = float(input("請輸入圓的半徑："))
circle(r)
'''''''''''''''''''''''''''''''''''''''''''''
def max(a, b):
    if a > b:
        return a
    else:
        return b

x = float(input("請輸入第一個數："))
y = float(input("請輸入第二個數："))

print(f"最大值是：{max(x, y)}")
'''''''''''''''''''''''''''''''''''''''''''''
def tw(year):
    return year + 1911

yeari = int(input("請輸入民國年份："))
print(f"西元年份：{tw(yeari)} 年")
'''''''''''''''''''''''''''''''''''''''''''''
def area(h, w):
    return abs(h) * abs(w)  
h = float(input("請輸入高度："))
w = float(input("請輸入寬度："))

print(f"矩形面積：{area(h, w)}")
'''''''''''''''''''''''''''''''''''''''''''''
def minutes(hr, mi):
    return hr * 60 + mi

a = int(input("請輸入小時："))
b = int(input("請輸入分鐘："))

print(f"總共是 {minutes(a, b)} 分鐘")
'''''''''''''''''''''''''''''''''''''''''''''
def min(total):
    hr = total // 60
    mi = total % 60
    return hr, mi

a = int(input("請輸入總分鐘："))

h, m = min(a)
print(f"{a} 分 = {h} 小時 {m} 分")
'''''''''''''''''''''''''''''''''''''''''''''
import array
a_list = ["1", 2, 3, 4]
a = array.array('f', [1, 2, 3, 4])
print(a)
print(a_list)
print(a[0])
for item in a:
    print(item)
for item in a_list:
    print(item)
'''''''''''''''''''''''''''''''''''''''''''''
import array
a = array.array('f', [1, 2, 3, 4])
a.append(5)
print(a)
a.insert(2, 10)
print(a)
