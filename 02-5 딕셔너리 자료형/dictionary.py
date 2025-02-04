# 딕셔너리(dictionary) : {key : value, , ,}
person = ['kim', 22, 111, True]
# print('person=', person)

person = {'name':'kim', 'age':28, 'height':181.5}
print("나이는 ",person['age'],'입니다.')

# 생성
di1 = {}
di2 = dict()

# 추가, 삭제 ([i] i는 인덱스가 아니라 키)
di = {1 : 'a', 2 : 'b'}
print('키가 2인 값 =', di[2])

di[3] = 'c'
print(di)

del di[1]
print(di)

test = {'name' : 'tom', 'score':88, 'score':95}
print('test=', test)

di = dict(a=1, b=True, c=3.14)
print('di=', di)

# 딕셔너리에 해당 키가 있는지 확인
bool_value = 'c' in di
print(bool_value)


# 키 : 값 수정하기
kv = {'a':10, 'b':20, 'c':30}
print('kv=', kv)
kv.update(a=90)
print('kv=', kv)

kv.update(e=70)
print('kv=', kv)

# 키가 숫자일때
kv = {1:'one', 2:'two'}
print('kv=', kv)

kv.update({3:'three'})

# 키 : 값 모두 가져오기(items, keys, values)
print(kv.items())
print(kv.keys())
print(kv.values())


# 키 리스트로 딕셔너리 만들기
keys = ['a', 'b', 'c']
di = dict.fromkeys(keys)
print('di=', di)

# 반복문 사용
x = {'a':10, 'b':20, 'c':30}
print('x=', x)
for e in x :
    print(e)

for k, v in x.items():
    print(k, v)

for i in x.keys():
    print(i)

print(x.values())

print('가장큰값 : ', max(x.values()))
print('총점 : ', sum(x.values()))
print('평균 : ', sum(x.values()))
