# 리스트 조작하기

# 요소추가(append, extend, insert)

a = ['a', 'b', 'c']
b = ['d', 'e']
a.extend(b)
print('a.extend(b) = {0}'.format(a))


a = ['a', 'b', 'c']
b = ['d', 'e']
a.append(b)
print('a.append(b) = {0}'.format(a))

a = ['a', 'b', 'c']
b = ['d', 'e']
a.insert(len(a), b)
print('a.insert(len(a), b) = {0}'.format(a))

# 요소 삭제하기(del 리스트[], pop, remove, clear)
a = ['a', 'b', 'c']
print(a)
a.pop()
print(f'a.pop() ={a}')
a.pop(0)
print(a)

li = ['a', 'b', 'x']
li.remove('x')
print(li)

# 리스트가 비어있는가 ? 아닌가?

li = []
print('li = {0}'.format(li))

bool("Hello")

if not li :
    li.append(100)
print(li)


# 리스트의 할당과 복사
a = list(range(3))
print('a = {0}'.format(a))

b = a
print(id(a), id(b))
print(a is b)
b.append(3)
print('a = {0}'.format(a))
print('b = {0}'.format(b))

a = [0,0,0]
b = a.copy()
print(f'a is b = {a is b}')
print(id(a),id(b))
b[2] = 99
print(a, b)

# 반복문(for, while) 사용
li = list(range(10))
print('li = {0}'.format(li))

for i in li :
    print(i, end='')

print()

for i in range(3) :
    print(i, end='*')

print()

for c in 'Hello':
    print(c, end='.')
    
print()

i = 0
while i < len(li):
    print(li[i], end='/')
    i += 1
print()

# 리스트 표현식 사용하기([식 for 변수 in 리스트])

a = [34, 52, 92, 14, 13]
for idx in range(len(a)) :
    a[idx] *= 100

print(a)

a = list(range(10))
print('a={0}'.format(a))

b = [i*100 for i in range(10)]
print('b={0}'.format(b))

c = [i for i in range(10) if i % 2 == 0]
print('c={0}'.format(c))

d = [i for i in range(10) if i % 2 == 1]
print('d={0}'.format(d))


# 구구단 출력 리스트 만들기
li = []
for i in range(8):
    for j in range(9):
        li.append((i+2)*(j+1))

print(li)
print()

li = []
for i in range(2,10):
    for j in range(1, 10):
        li.append(i*j)

print(li)
print()
e = [i*j for i in range(2,10) for j in range(1, 10)]
print('e={0}'.format(e))

# vars() : 선언한 변수 볼수있음
# dir(__builtins__) : 내장함수 볼수있음 

re = input("정수입력:")
print(re)
# 리스트에 map() 사용하기
# map은 리스트의 요소를 지정된 함수로 처리해준다.
li = list(map(float,range(10)))
print('li',li)

# a, b = input("두 정수입력:").split()
a, b = map(int,input("두 정수입력:").split())
print('a + b = 'a + b)
