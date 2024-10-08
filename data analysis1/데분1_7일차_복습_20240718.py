# -*- coding: utf-8 -*-
"""데분1_7일차.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QVH1yCwThDN7FCfz3egJPVFNLq1vQ18p
"""

#딕셔너리
cities = {'korea':'한국','japen':'일본','china':'중국'}
print(cities,type(cities))

#비어있는 딕셔너리 생성
di = {}
di2 = dict()
print(di,type(di))
print(di2,type(di2))

#딕셔너리의 값 수정
#딕셔너리명[key]=value
cities['japen']='Tokyo'
print(cities,type(cities)) #원래 일본이었던 japen의 value가 Tokyo로 변경되어서 출력

#딕셔너리의 key, value추가
#딕셔너리명 [key(현재 딕셔너리에 없는값)] = value
cities['germany']='베를린'
print(cities) #추가한 베를린이 딕셔너리에 추가되어 등장

#key value삭제
#.pop(key값)
cities.pop('japen')
print(cities) #japen과 일본삭제되어 출력
print(f"삭제할 값: {cities.pop('china')}")
print(cities) #중국과 일본 없어지고 한국과 베를린만 남음

#딕셔너리에 저장된모든 데이터 제거
cities.clear()
print(cities) #요소 전부 삭제되어 비어있는 딕셔너리로 출력됨

#딕셔너리의 메소드

cities = {'korea':'서울','japan':'일본','china':'중국','germany': '베를린'}
print(cities,type(cities))

#.keys(): 딕셔너리의 key값만 모아놓은 컬렉션을 만들어줌
print(cities.keys(),type(cities.keys())) #w자료형은 dict_keys이고 키값만 있는 컬렉션이 출력
print(list(cities.keys()),type(list(cities.keys()))) #키값들만 드러있는 값을 리스트로 형변환 하여 리스트로 만들어줌

for i in cities.keys():
  print(i) #키값만 모인 집합(리스트)을 for반복문의 집합형태로사용

#.values(): 딕셔너리의 values값만 모아놓은 컬렉션을 만들어줌
print(cities.values(),type(cities.values))#자료형은 dict_valeus이고 벨류값만 있는 컬렉션이 출력
print(list(cities.values()),type(list(cities.values()))) #벨류값만 리스트로 만들어서 출력

for i in cities.values():
  print(i) #벨류값만 모아놓은 리스트값을 for 반복문의 집합으로 사용

print()

#.items() : 키값과 벨류값을 하나의 튜플로묶어서 출력해줌
print(cities.items(),type(cities.items())) #키와 벨류값이 괄호로 묶여서 하나의 튜플로 출력됨

for i in list(cities.items()):
  print(i,type(i)) #값이 튜플로 반복되어서 나옴

for key, value in list(cities.items()):
  print(f"영문:{key}  한글:{value}") #튜플의 언패킹을 사용하여 딕셔너리의 items()값을
#각각 변수안에 넣어줌

print(key,value) #반복문 사용 후 변수로 출력해보면 반복문에서 맨 마지막으로 반복됐던
#germany와 베를린이 출력됨

print()

#.get()
#딕셔너리명.get(key값)입력하면 key값이 가진 value값을 반환해줌

di1={'봄':'꽃', '여름': '수박', '가을': '단풍', '겨울':'눈사람'}
print(di1,type(di1))

print(di1.get('봄'),type(di1.get('봄')))

#<실습>
#빈 리스트를 생성하고 for문을 사용하여 1~10까지 추가하기

#<로직구성>
#1)리스트 함수를 활용하여 리스트 생성
#2)for문과 range를활용하여 1~10까지의 숫자가 반복출력되도록 설계
#3)리스트 메소드 .append를 사용하여 반복된 값 리스트안에 추가


li1 = list()

for num in range(1,11):
  li1.append(num)  #꼭 여기서 결과를 출력할 필요는 없음.

print(li1)

print()

li2 = []

for num1 in range(1,11):
  li2.append(num1)
  print(li2)  #출력할때마다 쌓이는 누적 반복을 보고싶다면 출력된 최종결과를 볼 수 있도록
  #for문 안에 출력값을 넣으면 반복되면서 누적 출력값을 볼 수 있음

#<실습>
#음료자판기 프로그램 만들기
#버튼1 콜라, 2번 사이다, 3번 환타이고
#각 버튼에 따라 음료수 이름 출력하고
#그외 버튼이 입력될떄는 '제공하지 않은 메뉴'를 출력하기

#<로직구성>
#1) 음료자판기의 버튼을 key값으로, 음료의 이름을 value값으로 지정한 딕셔너리를 생성
#2) 계속해서 음료를 입력받아야하고, '그외의 버튼이 입력될때'라는 조건이 있기때문에 무한루프를 사용하고 if조건문을 활용
#3) 음료수 이름을 입력해야하기 때문에 input함수를 만들어줌

drink = {1:'콜라', 2:'사이다', 3:'환타'}

while True:
  name = int(input('음료의 번호를 입력하세요(1~3): '))
  if name in drink:
    print(drink[name])
    # print(drink.get(name)) 으로 get함수사용해서 출력해도 됨!
    break
  else:
    print('제공하지않은 메뉴')

#내장함수
#이미 파이썬 안에 내장되어있기때문에 따로 improt해줄 필요없이 바로 사용가능

#내장함수의 문자형 내장함수
#1) chr(): 괄호안에 아스키코드, 유니코드를 입력하면 해당 코드값을 가진 문자를 반환
print(chr(65),type(chr(65))) #65의 코드를 가진 문자인 A를 반환
print(chr(66),type(chr(66))) #66의 코드를 가진 문자인 B를 반환
print(chr(34),type(chr(34))) #34의 코드를 가진 문자인 "반환

print(chr(44032,),type(chr(44032))) #한글도 유니코드값을 가지기때문에 한글도 출력가능
print(chr(44033),type(chr(44032)))
print(chr(55034),type(chr(55034)))

print()

#문자형 내장함수 eval()
#문자형으로 전달된 표현식도 결과값을 반환해줌
print("100+200",type("100+200")) #100+200이라는 그냥 문자값. 자료도 str
print(eval("100+200"),type(eval("100+200"))) #300으로 계산됐고 자료형도 int로 출력
print("max(1,2,3,4,5)") #따옴표안에 넣었기때문에 max(1,2,3,4,5)라는 문자열
print(eval("max(1,2,3,4,5)"),type(eval("max(1,2,3,4,5)"))) #max값 계산되고 자료형 int

print()

#문자형 내장함수 format()
#입력받은 인수와 포멧코드에 따라서 형식을 갖춘 문자열을 반환. 포멧코드를 전달하지 않을 수 있으며
#전달하지 않을 경우 입력한 인수가 str로 반환됨(str함수를 호출한것과 결과가 같음))
print(10000,type(10000)) #숫자 10000이 입력되고 당연히 int로 출력
print(format(10000),type(format(10000))) #똑같이숫자형으로 입력했지만 자료형 str로 바뀜

print(format(10000000,','),type(format(10000000,',')))
#format에는 다양한 형태의 형식지정자(포멧코드)가 존재함. ,는 3자리수 마다 점찍어달라는 포멧코드
#이외에도 .(소수점 표시자리)f는 소수점 몇째짜리까지 표시할 수 있다.
print(format(2.43253,'.2f'),type(format(2.43253,'.2f')))
#소수점 둘째짜리까지 표현해달라는 뜻.
print(format(0.97,'.3%'),type(format(0.97,'.3%'))) #백분율 표시
#이렇게 포멧코드를 전달하면 해당 포멧코드에 맞는 형식으로 바뀌어서 전달해주고
#아무 코드도 입력하지 않으면 그냥 문자형으로 변환

print()

#문자형 내장함수
#str(): 전달받은 인수를 문자열ㄹ 반환
print(100,type(100))
print(str(100),type(str(100)))

#숫자형 내장함수 (정수, 실수 둘다 포함)

#abs():괄호안에 입력된 인수를 절대값으로 반환
print(-34,type(-34))
print(abs(-34),type(abs(-34))) #마이너스 표시 사라지고 정수값으로 출력
print(abs(-3.14),type(abs(-3.14))) #실수도 가능

print()

#divmod(): 입력된 두 인수의 몫과 나머지를 '튜플'로 반환
print(divmod(10,3),type(divmod(10,3)))#몫인 3과 나머지인 1을 튜플로 묶어서 반환
print(divmod(10,2),type(divmod(10,2))) #나머지가 남지않게 딱 떨어나눠지는 것들도 그냥 나머지0으로 반환해줌

print()

# float() : 정수를 실수로 변환
# int() : 실수를 정수로 변환
print(float(10),type(float(10))) #정수 10 입력하면 뒤에 .0붙여서 실수로 변환
print(int(23.3),type(23.3)) #실수뒤에 .3 없어져서 정수로 변환

#숫자형 함수

#max(최대값), min(최소값), sum(합계)
print(max(24,364,86,25,3)) #최대값 반환
print(min(24,23,15,352,35)) #최소값 반환
print(sum([12,2])) #전달된 리스트나 튜플과 같이 반복하는 객체의 합을 반환.
print(sum((1,2,3,4))) #바로 sum()괄호안에 적으면 에러. 괄호를 하나 더 만들어서 튜플로 값넣기

print()

#pow(값, 거듭제곱값) : 전달된 두 인수의 거듭제곱을 반환해줌. (**거듭제곱 연산자와 기능이 동일)
print(pow(12,2))
print(12**2) #거듭제곱연산자와 pow()값 동일
print(pow(10,2))

print()

#round(): 반올림값을 반환해줌
print(round(1.5),type(round(1.5))) #입력된 인수 1개이면 반올림하여 정수반환
print(round(2.5)) #반올림 안된이유: round함수는 앞자리의 수가 짝수라면 무조건 버림이됨: 오사오입의 법칙
print(round(2.34,1)) #입력된 인수가 2개라면 두번째 인수는 소수점이 몇번째 자리수까지 나올지 결정하는것
print(round(23.142,2))

#시퀀스의 내장함수
#enumerate():리스트와 함께 사용하며, 리스트안에있는 요소와 해당 요소의 인덱스번호를
#튜플로 묶어서 반환

li = ['가위','바위','보']
print(li,type(li))

print(enumerate(li1)) #enumerate는 그냥일반 출력문에서는 사용할 수 없음.
#일반 출력문으로 바로 출력하게 되면 클래스값으로 출력되기때문
#enumerate()의 값을 보려면 반드시 반복문을 통해 확인해야함

for i,j in enumerate(li):
  print(i,j)
#enumerate는 튜플로 묶어져서 나오기때문에 언패킹도 가능
#추출된 인덱스번호는 정수로 출력

print()

#range() : 숫자의 더미를 생성. 특정 범위를 지정할 수 있어 범위 지정자라고도 불림.
#다른 자료형으로 형변환 가능
print(range(1,10)) #일반 출력문으로는 요소의 값 확인이 불가하며 자료형은 range라고 나옴
print(list(range(1,11)),type(list(range(1,11)))) #range함수를 list로 형변환하여 값 확인
print(tuple(range(1,11)),type(tuple(range(1,11))))
print(set(range(1,11)),type(set(range(1,11))))
# print(dict(range(1,11)),type(dict(range(1,11))))#딕셔너리로는 형변환 안됨
print(list(range(0))) #range의 값을 0으로 하면 비어있는 리스트생성가능

print()

#len(): length의 줄인말로 전달된 객체길이 (항목갯수)를 반환해주는 함수
li = [1,2,3,4,5,6,"안녕",3.14,True]
print(len(li),type(len(li))) #리스트의 요소갯수 정수로 반환.

#문자열에서도 사용가능!
print(len('hello python'),type(len('hello python'))) #공백도 데이터이기때문에 포함해서 길이 반환
print(len('안녕하세요'),type(len('안녕하세요')))

#시퀀스의 내장함수

#sorted(): 전달된 반복가능 객체의 요소를 오름차순 정렬
#(메소드.sort()결과와 동일)

li2 = [5,3,2,9,0,1,4,7,3]
print(sorted(li2),type(sorted(li2))) #오름차순 정렬되어 작은 수 부터 정리
print(li2) #하지만 리스트만 출력하면 정렬 취소됨
#메소드.sort()는 원본자체의 정렬을 바꾸지만 sorted()함수는 원본자체를 바꾸진못함. 출력시에만 오름차순

li2.sort()
print(li2) #메소드는 원본자체가 변경된것을 알 수 있음

#sorted(reverse = True): 내림차순

print(sorted(li2, reverse = True)) #내림차순
print(li2) #내림차순도 마찬가지로 원본자체를 바꾸지 못함

print()

#zip
#전달된 여러개의 반복가능 객체의 각 요소를 튜플로 묶어서 반환하는 함수
#만약 전달된 반복가능 객체의 길이가 서로 다르면 길이가 짧은 반복가능 객체를 기준으로 동작
name = ['짱구' ,'철수','유리','맹구']
score = [74, 100, 90, 59]

print(f"{name[0]}의 점수는 {score[0]}점입니다")
print(f"{name[1]}의 점수는 {score[1]}점입니다")
print(f"{name[2]}의 점수는 {score[2]}점입니다")
print(f"{name[3]}의 점수는 {score[3]}점입니다")
 #두개의 컬렉션 값을 동시 출력하려면 이런방법으로 기존에 출력해야했음

print()

#zip와 반복문 사용

for i in range(len(name)):
  print(i) #길이 변환 함수로 name리스트의 값만큼 반복할 수 있도록 range로 다시 한번 감싸줌(총4번 반복)
  print(f"{name[i]}의 점수는 {score[i]}점입니다.") #rang때문에 순서대로 인덱스번호가 자동생성됨

print()

#zip
for sutdent in zip(name, score):
  print(sutdent) #튜플로 묶여있기때문에 언패킹을 하여 풀어줌!

print()

for sutdent, point in zip(name, score):
  print(f"{sutdent}의 점수는 {point}입니다.")

print()

name = ['짱구' ,'철수','유리','맹구', '훈이']
score = [74, 100, 90, 59]

for student , point in zip(name, score):
  print(f"{student}의 점수는 {point}") #두개의 길이가 맞지 않아도 짧은 리스트 기준으로
  #출력되기때문에 오류나지 않음.

# for i in range(len(name)):
#   print(i)
  # print(f"{name[i]}의 점수는 {score[i]}점입니다.")
  #zip를 쓰지않고 사용한 반복문의 경우에는 두개의 리스트 길이가 맞지않아서 오류가남

#<실습>
#<실습>
#월별 일수 리스트가 있을때 1월~12월과 마지막을 같이 출력
#[출력결과]
#1월 : 31일
#...
#12월 : 31일

#<로직구성>
#1)day의 길이가 1~12개로 맞기 때문에 인덱스 번호를 사용
#2)인덱스 번호를 사용할 것이기때문에 enumerate()함수 사요
#3)enumerate()함수의 값 사용을 위해 for 반복문사용
#4)언패킹으로 값 나눠서 출력

day=[31,28,31,30,31,30,31,31,30,31,30,31]

for month, date in enumerate(day):
  month+=1
  print(f"{month}월 : {date}일")

print()

for month, date in enumerate(day):
  print(f"{month+1}월 : {date}일") #f-string안에서 +해줘도 됨

#<실습>_같은 문제 zip사용해서 풀기
#zip  사용

month = [1,2,3,4,5,6,7,8,9,10,11,12]
day=[31,28,31,30,31,30,31,31,30,31,30,31]

for i,j in zip(month, day):
  print(f"{i}월 : {j}일")
