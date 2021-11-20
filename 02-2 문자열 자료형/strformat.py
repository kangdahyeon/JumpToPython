# 문자열 서식 지정자(%) 와 포매팅(format메서드) 사용하기

# %s
print('I am %s' % 'korean')

# %d
age = 28
st = 'I am %-10d years old' % age
print(st)

# %f
print("Error is %f%%" % 99.99)
print('%.3f'% 3.0) 
print('%10.2f' % 3.141592)



# 서식지정(%) 로 문자열 안에 여러 값 넣기
st = "Today is %d %s" % (16, 'no')
print(st)


#----------------------------------------------
# format 메서드 사용 : '{인덱스}'.format(값)
st = 'Hello, {0}'.format('world')
print(st)

st = '{0} {0} {1} {1}'.format('Python', 'Script')
print(st)

language = 'Python'
version = '3.10.0'
st = f'Hello,{language} {version}'
print(st)

# 천단위 콤마넣기 : format(숫자, ',')
st = format(10000000, ',')
print(st)

# 서식지정자 + format함수
st = '%20s' % format(345000, ',')
print(st)

# -----------------------------------------------
# Q. path = 'c://user//Appdata//local//program//python3//python.exe'
# print(filename)

