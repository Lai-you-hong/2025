pi = 3.14159
temperature = -10.5
scientific_notation = 2.5e6
'''''''''''''''''''''''''''''''''''
print(f"圓周率：{pi}")
print(f"溫度：{temperature}")
print(f"科學記號：{scientific_notation}")
'''''''''''''''''''''''''''''''''''
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")
print(f"是否等於 0.3: {result == 0.3}")
'''''''''''''''''''''''''''''''''''
a = int(input("數字一"))
b = int(input("數字二"))

print(f"加法：{a} + {b} = {a + b}")
print(f"減法：{a} - {b} = {a - b}")
print(f"乘法：{a} * {b} = {a * b}")
print(f"除法：{a} / {b} = {a / b}")
print(f"整數除法：{a} // {b} = {a // b}")
print(f"餘數：{a} % {b} = {a % b}")
print(f"次方：{a} ** {b} = {a ** b}")
'''''''''''''''''''''''''''''''''''
age = 1
score = 60

age_str = str(age)
score_str = str(score)

print(f"整數 {age} 轉字串：'{age_str}' (型別：{type(age_str)})")
print(f"浮點數 {score} 轉字串：'{score_str}' (型別：{type(score_str)})")
'''''''''''''''''''''''''''''''''''
str_number = "10"
str_float = "3.14"

int_number = int(str_number)
float_number = float(str_float)

print(f"字串 '{str_number}' 轉整數：{int_number} (型別：{type(int_number)})")
print(f"字串 '{str_float}' 轉浮點數：{float_number} (型別：{type(float_number)})")
