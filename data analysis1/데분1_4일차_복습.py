# -*- coding: utf-8 -*-
"""데분1_4일차 복습.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vUEGbuTYv8O81MvFgX4cPEuo2d2iXWlU
"""

#튜플(tuple)
#리스트와 거의 동일하지만 한번 생성하면 수정이 불가능 ->읽기전용 리스트라고도 불림

tu1=(1,2,3,'안녕',True,1.1) #모든 자료형 삽입가능, 중복값도 허용!
print(tu1,type(tu1))

#시퀀스 자료형_인덱싱 / 슬라이싱 둘다 가능
#인덱싱
print(tu1[3],type(tu1[3])) #'안녕'추출! 인덱싱이기때문에 문자형으로 추출
print(tu1[4],type(tu1[4])) #4번째인 논리형으로 추출

#슬라이싱
print(tu1[0:3],type(tu1[0:3])) #슬라이싱 했기때문에 자료형은 tulple

#튜플의 특징_packing(패킹)/unpacking(언패킹)
#packing(패킹) : 여러가지 자료형을 튜플로 묶어주는것!
tu2= 1,2,3,1,2,3,'패킹'
print(tu2,type(tu2)) #소괄호를 사용하지 않아도 소괄호로 묶여출력되며 자료형도 튜플!
tu3=1
print(tu3,type(tu3))#튜플의 값이 한개일때 그냥 tu3이라는 변수에 그 한개의 값을 넣어준 것이기때문에 tu3의 자료형은 int임 튜플이 아님
tu3 = 1,
print(tu3,type(tu3)) #패킹할때 값이 하나이더라도 뒤에 콤마를 작성해야 튜플로 패킹됨
tu3= (1,)
print(tu3,type(tu3)) #일반 튜플 생성할때도 똑같이 값이 하나라면 콤마 무조건 작성

#unpacking(언패킹):튜플의 요소를 여러개의 변수에 할당
print(tu2,type(tu2))#7개의 값이 들어가 있음
num1,num2,num3, num4,num5,num6,num7= tu2
print(num1,type(num1)) #패킹되어있던 값들을 풀어서 해당 변수에 순서대로 넣어줌
print(num7,type(num7))
#unpacking된 값은 본래가지고있던 기본 자료형으로 출력
#*unpacking할때 값의 갯수와 변수의 갯수가 동일해야함. 그러지 않으면 오류!*

#in, not in연산자 사용
#튜플에서도 in not in연산자 사용이 가능함
print(1 in tu2,type( 1in tu2))#1이라는 값이 tu2안에 있니? => 있어!(True)로 출력하기 때문에 자료형은 논리형
print(2 not in tu2)

#시퀀스 연산자 사용
#튜플은 시퀀스 자료형이기때문에 시퀀스 연산자 사용가능 (+,*)
print(tu1+tu2,type(tu1+tu2)) #튜플2개의 값이 하나의 튜플로 연결되었고 자료형도 튜플로 출력
print(len(tu1+tu2),type(len(tu1+tu2))) #len로 값 갯수 출력하면 두개의 값이 합쳐져서 13출력
print(tu1*2,type(tu1)) #두번반복되고 결과 튜플

#세트{set}
#세트는 중복값을 가질 수 없음. 비시퀀스 자료형(시퀀지연산자 사용X  인덱스, 슬라이싱 사용X)

set1 = {1,2,3,1,2,3}
print(set1)#중복값을 넣는다고 해서 오류가 나는것은 아니지만 출력할때 중복값 제외하고 출력
# print(set1[1])#인덱스 사용불가!
# print(set1*2)#시퀀스 연산자 사용불가!


#컬렉션의 형변환_중복제거 set
#컬렉션 형변환 할때 set를 사용하면 리스트와 튜플의 중복값을 제거하여 set로 만들 수 있다
#set() =>>set로 형변환해주는 함수
li1 = [1,2,3,1,2,3]
print(set(li1),type(set(li1)))#기존 리스트에서 중복값이 제거되었고 자료형도 세트로 형변환
li2=[1,2,3,1,2,3,'안녕','안녕']
print(set(li2),type(set(li2))) #변수 안쓰고 print문에서 바로 형변환 가능

#list()=>> list로 형변환해주는 함수
set2 = set(li1)
print(set2,type(set2)) #현재 세트로 형변환되었기때문에 세트로 출력!
li2= list(set2)
print(li2,type(li2)) #리스트로 다시 형변환이 되었음

#tuple()=>>tuple로 형변환해주는 함수
tu1= 1,2,3,4,1,2,3 #패킹으로 tuple만들기
print(tu1,type(tu1)) #자료형 튜플
set3 = set(tu1)
print(set3,type(set3)) #중복값 제거되고 자료형 세트로 출력
tu1 = tuple(set3)
print(tu1,type(tu1)) #세트였던 set3을 다시 tu1이라는 변수안에 튜플로 형변환하여 다시 튜플로 출력됨

#세트는 비시퀀스이기때문에 순서가 뒤죽박죽 출력될 수 있음
set4= {1,2,3,"안녕",True, 1.0,1.1}
print(set4) #"안녕"이 제일 끝으로감. 세트는 1이나 1.0이나 같다고 판단되기때문에 1.0이 중복값으로 체크되어 사라짐

#딕셔너리(dict)
# key : value의 형태
#비시퀀스 자료형이므로 인덱싱, 슬라이싱 불가
#하지만 key를 인덱스 번호처럼 사용할 수 있음 => key는 중복 X value는 중복 가능하며 어떤 자료형도 다 들어갈 수 있음

di1 ={"A":1, "B":2}
print(di1,type(di1)) #자료형 딕셔너리

di2={"A점":["짱구","철수","유리","훈이"],"B점":"맹구" }
print(di2,type(di2))#"A점"안에 리스트를 활용하여 여러가지의 값 넣기 가능

#key로 value접근하기
#딕셔너리명[key]
print(di2["A점"],type(di2["A점"]))#"A"점에 저장된 값이 나오고 자료형은 리스트
print(di2["B점"],type(di2["B점"])) #"B"점에 저장된 맹구가 나오고 자료형은 문자형

#keys() , values()
#딕셔너리의 key값만 추출하기
print(di2.keys,(),type(di2.keys())) #딕셔너리명.keys #key값인 A점과 B점만 나옴. 자료값은 딕셔너리의 키값!
#딕셔너리의 value값만 추출하기
print(di2.values(),type(di2.values()))#딕셔너리명.values() #values값인 이름들이 나옴. 자료값은 딕셔너리의 벨류값!

#딕셔너리의 튜플. =>> items
print(di2.items(),type(di2.items()))# 딕셔너리의 키와 벨류를 하나의 튜플로 묶어서 출력

#비어있는 컬렉션 생성하기

#1)비어있는 리스트만들기 : (1):빈 대괄호 사용[]  / (2)list()함수 사용하기
li1 = []
print(li1,type(li1)) #값이 비어있는 리스트 출력
print(bool(li1),type(bool(li1))) #bool자료형에서 빈값들은 전부 False반환하기때문에 bool자료형으로 변환하면 False출력
li2=list()
print(li2,type(li2)) #리스트 함수를 이용하여 만든 값이 비어있는 리스트
# li3 = list(1,2,3,4)
# print(li3)#에러발생. list()함수는 비어있는 리스트를 생성하거나 리스트로 형변환을 할때만 사용

#2)비어있는 튜플만들기: (2)빈 소괄호 사용() /tuple()함수 사용하기
tu1 = ()
print(tu1,type(tu1)) #값이 비어있는 튜플 출력
print(bool(tu1),type(bool(tu1))) #튜플도 bool함수로 변환하면 빈괄호 이기때문에 False출력
tu2=tuple()
print(tu2,type(tu2)) #tuple함수를 사용하여 빈 튜플 만들기
# tu3 = tuple(1,2,3)
# print(tu3,type(tu3)) #튜플도 tuple함수를 이용하여 튜플생성X

#3)비어있는 세트 만들기 : set()함수 이용하기
set1 = {}
print(set1,type(set1)) #자료형 dict으로 나옴. 세트는 빈중괄호 사용해서 빈 세트 못 만듬!
set2=set()
print(set2,type(set2)) #set()함수를 이용하면 빈 세트 만들기 가능!
#※set는 {}중괄호만을 이용하여 빈 세트 못만듬. 오로지 set()함수만 이용하기※#

#4)비어있는 딕셔너리만들기 : (1)빈 중괄호사용 {} / dict()함수 사용하기
di1={}
print(di1,type(di1)) #빈 중괄호 사용해서 비어있는 딕셔너리 만들기
di2 = dict()
print(di2,type(di2)) #dict()함수를 이용하여 비어있는 딕셔너리만들기

#<복습 겸 실습>_조건문을 위한 논리연산자
#두개의 정수를 입력받아 두 정수 중 하나라도 양수라면 True출력
#둘다 양수가 아니라면 False출력

#논리 연산자만 사용
num3= int(input('첫번째 정수입력: '))
num4=int(input('두번째 정수입력: '))
print(num3>0 or num4>0)

#논리연산자+삼항연산자
num1= int(input('첫번째 정수 입력: '))
num2= int(input('두번째 정수 입력: '))
result='True' if num1>0 or num2>0 else 'False'
print(result)

#둘중 하나라도 양수이기만 하면 되니까 and가 아닌 or를 사용하여 출력

#<복습 겸 실습>_조건문을 사용한 논리연산자 2
#파이썬 점수가 80점이상이고 자바 점수가 60점 이상이라면 '시험합격' 출력
#그외는 시험 불합격 출력

python = int(input('python점수를 입력하세요: '))
java = int(input('java점수를 입력하세요: '))
result1 = "시험합격" if python>=80 and java>=60 else "시험 불합격"
print(result1)

#삼항 연산자처럼 출력값으로 받고싶은 다른 출력값이 있는게 아니라
#출력값이 Ture 나 False라면 print()출력문에 바로 적어주면 됨

#if조건식

#if 조건식 작성 :
#  (들여쓰기 필수) print(if문 안에있는 문장) #if문의 조건식이 True일때 출력되는 문장
#print("if문 밖의 문장") #if문 밖의 문장이기때문에 들여쓰기 X 조건식과 상관없는 문장. if문의 조건식이 False일때 True가 건너뛰어지고 얘만 출력됨

print("----if문이 참인경우----")
if True :
  print("if문안의 문장. 참일때 실행")
print("if문 밖의 문장. 조건식과 상관없이 출력\n")

print("----if문이 거짓인경우----")
if False :
  print("if문안의 문장.")
print("if문 밖의 문장.\n")#조건식이 참일때 실행되는 if문 안의문장이 건너뛰어지고 if문 밖의 문장만 실행된것

print("----if문이 거짓인데 if문 밖의 문장이 없는경우----")
if False :
  print("if문안의 문장. 참일때 실행")
#아무것도 출력되지 않음
#단순if문은 참일때만 실행이 되는것이기때문에 거짓일때 실행할 문장이 따로 없음

#if문 <실습>
#사용자로부터 숫자를 입력받고, 입력받은 숫자가 100이라면 "100입력!" 단어를 출력

num1 = int(input("숫자를 입력하세요: "))

if num1==100:
  print("100입력!")
print("프로그램 종료")#100이외의 값을 넣으면 if문의 조건식에 거짓됨으로 "100입력!"이라는 단어출력X

#if ~ else조건문
#if조건문이 거짓일때 실행할 문장을 else문에 적어줌

print("----if문이 참인경우----")
if True :
  print("if문 안의 문장 / if문의 조건이 참일때 실행")
else:
  print("else문 안의 문장 / if문의 조건이 거짓일때 실행")#참이기때문에 else문 출력X
print("else문 종료 / if문 밖의 문장 / if문과 상관X\n")

print("----if문이 거짓인 경우----")
if False :
  print("if문 안의 문장 / if문 조건이 참일때 실행")#거짓이기때문에 if문 출력X
else :
  print("else문 안의 문장 / if문의 조건이 거짓일때 실행")
print("else문 종료 / if문 밖의문장 / if문과 상관X\n")

#<if~else문 실습>
# 사용자로부터 정수를 입력받아 입력받은 정수가 짝수라면 짝수 출력
# 그게 아니라면 홀수 출력

num1 = int(input('정수입력: '))

if num1%2==0:
  print("짝수")
else:
  print("홀수")

#<if~else문 실습2>
# 사용자로부터 정수를 입력받아 입력받은 정수가 2와 3으로 나누어 떨어지면
# 나누어 떨어집니다 출력 그게 아니라면 나누어 떨어지지 않습니다 출력

num1 = int(input('정수입력: '))

if num1%2==0 and num1%3==0:  #나머지가 0이여야 딱 나누어 떨어지는것!
  print("나누어 떨어집니다")
else:
  print("나누어 떨어지지 않습니다")
print("프로그램 종료")

#if ~ elif~else 문
#조건식이 최소 2개이상은 작성되어야함(if문 조건식과 elif문 조건식)
#elif는 여러개 작성이 가능하고, elif가 여러개 있을시 가장 위에있는 조건부터 순차적으로 작성!

num=25

if num >20: #if문 조건식에 충족되기때문에 if문이 출력되고 바로 종료
  print("num이 20보다 큽니다")
elif num>=10:
  print("num이 10이상 20이하 입니다")
elif num>=5:
  print("num이 5이상 10이하 입니다")
else:
  print("num이 5미만 입니다")
print("프로그램 종료\n")

num1=10
if num1>20:
  print("num1이 20이상입니다")
elif num1 >=10:
  print("num1이 10이상입니다") #num1이 10이기때문에 if문을 건너뜀. 첫번째 elif가 참이기때문에 실행하고 종료
elif num >=5:
  print("num1이 5이상입니다")
else:
  print("num1이 5보다 미만입니다")
print("프로그램 종료\n")

num2=5
if num2>20:
  print("num2가 20이상입니다")
elif num2>=10:
  print("num2가 10이상입니다")
elif num2>=5:
  print("num2가 5이상입니다") #num2가 5이기때문에 if문과 첫번째elif문을 건너뛰고 두번째 elif문 출력
else:
  print("num2가 5미만입니다")
print("프로그램 종료\n")

#if~if문
#모든 조건을 if문으로 작성하면 출력결과는 조건식이 True인 모든 결과가 출력된다

num3 = 25  #만약 20보다 작은 수로 변수 변경하면 첫번째 if문은 출력되지 않음

if num3>20:
  print("num3이 20보다 큽니다") #num3이 25이기때문에 해당
if num3>=10:
  print("num3이 10이상입니다") #num3이 25이기때문에 해당
if num3 >=5:
  print("num3이 5이상입니다") #num3이 25이기때문에 해당
print("프로그램 종료")

#모든 if문이 출력됨
#if문는 순차적으로 실행될때 무조건 먼저 실행됨.
#그냥 서로다른 if문이 나열된것뿐 문법적으로 오류가 있는 상태는 아님!
#모든 조건문을 if문으로 작성하면 출력결과가 True인 모든 결과가 출력이 되는것뿐!
