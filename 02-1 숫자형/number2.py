#정수형
a = -178
print(a)

#실수형
a = 3.14E-2
print(a)

#n진수
a = 0b1001
print(a)
a = 0o11
print(a)
a= 0xabc
print(a)
#제곱표시 **
print(2**10)
a = 0xabc
print(a)
print(10*16**2 + 11*16 + 12)


# 연산
a = 3; b = 4
print (a + b)
print(3**4)
print(3/4)
print(3//4)
print(7%3)


# 파이썬에서의 정수(integer)
i1 = 9999999999999999999999999999999999999999999999999999
i2 = 1
print(i1)
print(i1+1)
print(type(i1))
# i 는 클래스로 자바로 치면 래퍼클래스
print(i1.bit_length())
print(i2.bit_length())

#arbitrary-precision <-> fixed-precision

# 파이썬에서의 실수(float)
print(3.5 + 2.1)
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(round(4.3 - 2.7, 15))

#파이썬에서의 형변환 및 연산
print(int(3.14))
print(float(5))
x = '3.14'
print(type(x))
y = float(x)
print(type(y))
print('111' * 3)
print('111\n' * 3)
#print("111" + 1) -> 오류남

