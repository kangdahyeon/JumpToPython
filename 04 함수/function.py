# 함수
def add(a, b):
    return a + b

result = add(5, 3)
print('result =', result)


# 함수 독스트링(docstrings) 사용

def multi(x, y):
    """multi(x, y): x * y 결과값을 리턴한다."""
    return x*y

re = multi(5,3)
print(multi.__doc__)
print('re=', re)

# 값을 여러개 반환하기
def add_sub(a, b):
    return a+b, a-b
re = add_sub(30, 20)
print(type(re))
print('re=', re)

r1 , r2 = add_sub(30, 20) # 언패킹
print(r1)

# 몫과 나머지 구하기
def get_qr(x, y):
    return(x//y, x%y)
result = get_qr(7, 2)
print('get_qr(7, 2) : 몫 =', result[0], '나머지=', result[1])

def print_params(a, b, c):
    print(a)
    print(b)
    print(c)
print_params(1,2,3)
# 언패킹 사용하기: 함수명(*리스트 *튜플)
xl = [10, 20, 30]
print_params(*xl)


# 가변인수(variable argument): 인수의 갯수가 정해지지 않을때
def print_args(*args):
    for e in args:
        print(e)

print_args('a', 'b', 'c')

print_args(10,20,30,40,50,60,70)

print_args(True)

# 키워드 인수 사용하기
def print_info(name, age, phone):
    print('이름:', name)
    print('나이:', age)
    print('번호:', phone)

print_info("철수",20,'010-') # 인수의 순서를 기억해야함.
print_info(age=20, phone='010', name='dd')

print('=='*20)

# 딕셔너리 가변 인수 함수
def print_dict(**args):
    for k, v in args.items():
        print(k, ':', v)

print_dict(name='철수', age=27, addr='서울 강남구')
