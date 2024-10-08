# -*- coding: utf-8 -*-
"""데분1_5일차.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wlL-nJg-FcWa5uPuY2pVXW3N6Npj9Up8
"""

#<실습>
# 나이를 입력받아 입장료를 계산하는 프로그램
# 10세 이하의 입장료는 1000원, 65세 이상의 입장료는 0원
# 기본 입장료는 2000원
# 입장료 출력

#<로직구성>
#1) 나이를 입력받기 위한 input함수 설계
#2)입장료를 판단하기 위해 최소 변수3개 or 조건3개 필요
#3) 10세이하와 65세 이상은 해당하는 조건이 있기때문에 그외는 나머지로 처리가능

#!)if~elif~else문을 이용한 방법
#-여기서는 조건 실행문을 통해 입력
age = int(input("나이를 입력하세요: "))

if age >=65:
  print("입장료: 0원")
elif age <= 10:
  print("입장료: 1000원")
else :
  print("입장료: 2000원")

print()


#2)조건을 변수로 입력하는 방법

age1 = int(input("나이를 입력하세요: "))

if age>=65:
  price = "0원"
elif age <=10:
  price = "1000원"
else :
  price = "2000원"

print(f"{age}세의 입장료는 {price}입니다")


#-------------------------------------------#
#1,2번의 차이점
#1번 둘다 동일하게 input함수로 나이를 입력받고 입장료까지 출력이 동일하게 됐지만
#1번의 경우에는 결과값을 조건문에 넣었음 =>> 틀린것은 아니지만 조건문에 입력한대로만 출력할 수 있어, 값을 유연하게 수정하거나 할 수없음
#2번의 경우에는 조건문 출력부분에 변수를 넣어, 각 조건문이 참일때 변수가 출력되도록함. 또한 마지막 부분에 f-string을 이용하여 최종출력문을 유연하게 수정할 수 있도록 하였음
#그 대신 2번의 경우에는 마지막 print문이 없다면 input함수만 나오고 일반 변수는 그냥 정의만 된 상태이기때문에 꼭 결과를 볼수있도록 출력문을 마지막에 만들어주어야함

#<실습>
#성적을 입력받아서 학점 출력하는 프로그램
#90점이 이상A
#80~89 B학점
# #70~79 c학점
# 60~69 D학점
# 그외 F학점
# 학점 출력

#<로직구성>
#1)성적을 입력받아야하기때문에 각 성적 input함수 만들어주기
#2)A,B,C,D,F가 출력되어야하기 때문에 최소 조건5개 필요
#3)조건이 다양하기 때문에 if~elif~else조건 필요

#!)if~elif~else문을 이용한 방법
#-여기서는 조건 실행문을 통해 입력

score = int(input("성적 입력: "))

if score >=90:
  print("학점:A")
elif score >=80:
  print("학점:B")
elif score >=70:
  print("학점:C")
elif score >=60:
  print("학점:D")
else :
  print("학점:F")

print()

#2)조건을 변수로 입력하는 방법
#국어, 영어, 수학점수 입력받아 합산 점수가 250이상이라면 A학점
#249이하 150점 이상이라면 B학점
#149이하 100이상라면 C학점
#99이하 50이이상라면 D학점
#그외 F학점

#<로직구성>
#각 과목마다 input변수 설정
#각 과목 합산점수 계산하는 변수
#각 과목을 알려주는 변수 설정
#맨 마지막 출력문 형태. "{국어}{영어}{수학}점수. {학점}입니다"

kor=int(input("국어점수 입력: "))
eng=int(input("영어점수 입력: "))
math=int(input("수학점수 입력: "))

print()

if kor+eng+math>=250:
  score = "A학점"
elif kor+eng+math>=150:
  score = "B학점"
elif kor+eng+math>=100:
  score = "C학점"
elif kor+eng+math>=50:
  score = "D학점"
else :
  score = "F학점"

print(f"국어점수: {kor}\n영어점수: {eng}\n수학점수:{math}으로\n7-총 합산점수{kor+eng+math} / {score}입니다")

#while 반복문
#while조건식:
#(들여쓰기)조건식이 참일동안 반복실행할 문장

while True:
  print("조건문이 참일동안 반복실행할 문장")
#while문 뒤에 있는 조건문이 참인지 거짓인지 판별하는데 계속 트루이기때문에 끝없이 반복됨. = 무한루프 상태
#while문은 while문 안의 반복할 문장들 실행 후 다시 조건식으로 돌아감
  break #반복문 강제종료언어. 강제종료도 while문의 일부이기때문에 들여쓰기 필수!
#break를 만나는 순간 즉시 반복문을 탈출하여 강제 종료
print("while문 종료")#while문과 상관없는 while문 밖의 문장

#다시 한번 실행하면 한번만 실행하고 break를 만나서 강제종료됨.

print()
print()

while False:
  print("조건문이 참일동안 반복실행할 문장")
print("while문 종료")
#while문의 조건이 거짓이기때문에 반복 아예 반복문 안으로 들어가지도 않고 바로 반복문 탈출하여
#while문 밖의 문장이 실행된 것

#<while문 실습1>
#1~100까지의 정수를 가로로 출력

#<로직구성>
#정수1이 들어있는 변수 설정
#가로로 출력해야하기때문에 디폴트 줄바꿈이 되어있는 end를 다른것으로 바꿔주어야함
#정수1이 들어있는 변수가 100이 되었을때 반복문을 탈출하도록 다른 조건 설정

#가로로 바꿔주려면 기본으로 출력되는 디폴트를 다른것으로 바꿔주면 가로로 출력됨
#애초에 세로로 출력이되는 이유가 기본 디폴트인 줄바꿈 떄문!!

num=1

while num<=100:
  print(num,end=" ")
  num+=1   #복합 연산자를 이용하여 반복이 될때마다 num변수에 1씩 더해지도록 함.
print("정수 출력 종료")

#일단 num에 1이 들어가있으므로 100이하라는 조건에 True로 결과 출력
#그런다음 while문 영역안의 조건인 num+1을 해줌. 현재 num에 1이 있기때문에 하나가 더해져서 2가된채로
#다시 while문의 조건에 있는 num으로 들어감. 2도 100이하이기때문에 다시 반복.

#<while문 실습2>
#1시부터 시작해서 7시가되면 알림이 울리는 프로그램만들기(while 문사용)
#<출력결과>
#1시
#2시
#...
#7시가 되었습니다. 알람이 울립니다.

#<로직구성>
#시간(숫자)가 들어있는 변수 설정
#7과 동일해지면 반복문이 멈추도록 조건 설정
#시간을 알려주다가 맨 마지막에만 알람관련 문장이 나와야하므로 맨마지막 문장은 while문 밖으로 빼서 f-strin이용하여 출력

time=1

while time <=6: #time<7이렇게 해줘도 복수정답! 7미만이면 6까지만 출력되기때문에
  print(time,"시")
  time+=1
print(f"{time}시 입니다. 알람이 울립니다.")

#while time <=6:
#7시에 울려야하는데 7이하라고 쓰지않은이유:
#이미 반복문이 1시부터 계속되어 6까지 출력이 된후에 조건에 time+=1더해진채로
#다시 반복문의 조건문에 대입되기때문에 7이하라면 7도 포함되기때문에 반복문이 멈추는것이 아니라 그냥 7시로 출력되고
#다시 time+=1이 더해져서 8인채로 변수에 저장됨. 조건문인 7이하에 8은 안들어가기 때문에 이미 변수에는 7이아니라 8이저장되어있기때문.

print()

time=1

while time <=7: #time<7이렇게 해줘도 복수정답! 7미만이면 6까지만 출력되기때문에
  print(time,"시")
  time+=1
#특정숫자를 뽑고싶은것이 아니라 그냥 7시도 똑같이 "7시"의 형태로 출력하고싶다면 그냥 7이하라고 적으면 됨!
#하지만 변수에는 이미 time+=1이 적용되어 멈춘것이기 때문에 출력해보면 8로 나옴
print(time) #변수 8

time = 1

while True:
  print(f"{time}시")
  time+=1
  if time >=7:
    break

print(f"{time}시가 되었습니다. 알람이 울리니다.")

#<while문 실습2-1>
#1시부터 시작해서 7시가되면 알림이 울리는 프로그램만들기(while 문사용)
#<출력결과>
#1시
#2시
#...
#7시가 되었습니다. 알람이 울립니다.
#단 if 조건문과 함께 사용하기


#<로직구성>
#정수 1 이 들어있는 변수 설정
#if문을 사용할 것이기때문에 무한 루프로 계속 반복시켜줄것
#if문을 사용하여 해당 조건을 만족시켜주고 조건이 참일경우 조건문이 강제종료되도록 break함수쓸것



time = 1

while True:  #if문을 사용하여 종료해줄것이기 때문에 계속반복되도록 무한루프 생성
  print(f"{time}시") #계속 반복되면서 n시라고 출력되도록 f-sting으로 설정
  time +=1 #계속1시만 반복되는것이 아니라 +1씩 늘어나도록 변수 설정 #
  #조건문 안에 있는 변수는 조건문 안에서만 유효함. 즉 조건문 밖에서 사용불가
  if time >=7: #if문을 설정하여 반복되다가 time이 7이되면 문장 출력하도록 조건추가
    print(f"{time}시 입니다. 곧 알람이 울립니다")
    break #7이 됐으니 종료되도록 강제 종료언어인 break추가.
#if문으로 조건준다고 종료되는것이 아님! 만약 위의문장에서 break쓰지 않는다면 그냥 반복되다가 7이 됬을때만 해당 문장을 출력하고 계속 n시의 형태로 반복됨#

#<#<while문 실습3>
#정수입력받아 입력받은 정수가 1에서 10사이의 숫자라면 입력한 숫자 출력 ->반복문 탈출
#그게아니라면 1 ~10사이의 숫자를 다시 입력해주세요 출력
#다시 숫자 입력

#<로직구성>
#정수 입력받을 input변수 설정
#'아니면'이라는 조건이 들어갔기때문에 if~else사용
#if문 사용할것이기때문에 while문은 무한반복으로 사용하고 1~10사이의 수 조건은 if문에서 작성

while True:
  num=int(input("숫자를 입력하세요: "))
  if num>=1 and num<=10:
    print(f"입력하신 숫자:{num}입니다.3")
    break
  else:
    print("숫자를 다시 입력하세요")

#<#<while문 실습3>
#정수입력받아 입력받은 정수가 1에서 10사이의 숫자라면 입력한 숫자 출력 ->반복문 탈출
#그게아니라면 1 ~10사이의 숫자를 다시 입력해주세요 출력
#다시 숫자 입력

#<오답노트>

#1)num =int(input("숫자를 입력하세요: "))

# while True:
#   if num>=1 and num<=10:
#     print(f"입력한 숫자는{num}입니다.")
#     break
#   else:
#     print("숫자를 다시 입력해주세요")

#조건에 맞게 1~10사이의 수를 입력했다면 제대로 출력됨. 하지만 예로 조건에 맞지않은 11을 입력하면
#else문이 whil문안에 있기때문에 while은 일단 무한루프로 계속 반복되는 상황에서 조건에 맞지않아 else문이 계속 반복되는것. (변수는 몇번을 확인해도 11이니까)

#---------------------------#

#<로직 수정>
#조건에 맞지 않는 숫자가 입력되었다면 조건에 맞을때까지 숫자가 다시 입력되어야하기때문에
#숫자를 입력받을 input함수가 while문 안에 존재해야함!!!
#숫자를 입력받을 수 있는 변수가 while문의 밖에 있기때문에 그냥 변수를 참고한거지 while문과 상관이 있는것은 아닌 상태임

while True:
  num=int(input("숫자를 입력하세요: "))
  if num>=1 and num<=10:
    print(f"입력하신 숫자:{num}입니다.")
    break
  else:
    print("숫자를 다시 입력하세요")

#input변수도 다시 반복될 수 있도록 while문 안쪽으로 넣어줌
#그럼 입력받은 num변수를 if문의 조건에 맞는지 확인하고 맞다면 해당 출력문 출력하고 break를 통해 반복문 종료
#그게 아니라면 while문안에 있는 else문을 통해 숫자를 다시 입력하라는 문장이 나옴. 반복문 안에 있기때문에 else문 출력하고 다시 whil문으로 반복
#다시 input함수가 출력

#반복 for문
#for 변수명 in 집합:
#(들여쓰기)반복할 문장

str1="안녕하세요"
print(str1,type(str1)) #일반적인 str형태의 값으로 출력

for i in str1: #str1이라는 변수안에는 "안녕하세요"라는 변수가 저장되어있음
  print(i) # print(i,end=" ")라고하면 가로로 출력가능

#문자는 시퀀스자료형이기때문에 인덱스번호를 가지고 있고 for문은 이걸 집합의 형태로 인식
#'안'이라는 '안녕하세요'라는 집합의 첫번째 문자를 가지고 온것. 범위가 끝날때까지이다 보니
#for문은 지정된 범위가 끝날때까지 반복이다보니 '요'에 도달할때까지 반복출력된것
#str1변수에는 개별로 저장해준것이 아니여도 문자는 시퀀스 자료형이기때문에 for문 안에서 한글자씩 가지고 오는것이 가능함!

print()

# for i in 123: <<=에러 발생! (1,2,3)이라는 집합이 아니라 그냥 숫자 123인것.
#   print(i)
# #숫자는 시퀀스 자료형이 아니기 때문에 하나씩 가져오는거 안되고,
# #for문은 집합안에 있는 값들을 순서대로 가져오는건데 그냥 숫자 123이라고 인식했기때문에 당연히 에러!

for i in "hello python":
  print(i,end="") #공백도 시퀀스자료형으로 인정하기때문에 for문에서도 공백 추출가능. end옵션을 이용하여 가로 출력

print()

li1 = ['문자열', '문자', 1.5,3,True]
print(li1,type(li1)) #자료형 list

for i in li1:
  print(i,type(i)) #for문으로 출력하면 리스트안에 있던 자료형들이 전부 개인자료형으로 출력됨

print()

tu1= "문자열", "문자", 1.5, 3, True #튜플 패킹으로 튜플만들어준 것
print(tu1,type(tu1)) #자료형 튜플로 출력

for i in tu1:
  print(i,type(i)) #튜플도 동일하게 개인 자료형으로 출력

print()

set1 = {"봄","여름","가을","겨울"} #세트는 인덱스번호 없기때문에 순서 뒤죽박죽
print(set1,type(set1)) #자료형 세트로 출력

for i in set1:
  print(i,type(i)) #세트도 동일하게 개인 자료형으로 출력

#<for문과 tuple>

li2 = [(1,2),(3,4),(5,6)]
print(li2,type(li2)) #자료형 리스트 출력

for i in li2: #집합 자료형 = 리스트
  print(i,type(i)) #출력결과 자료형 = 튜플
#리스트안에는 다양한 자료형이 들어갈 수 있음. 튜플도 삽입가능한데, 지금 li2안에 3개의 튜플이 저장되어있고
#for문은 튜플1개당 1개의 자료형으로 인식하여 반복한것!!

print()

for i, j in li2:
  print(f"i:{i},j:{j}",type(f"i:{i},j:{j}")) #괄호안의 튜플값 2개, 변수가 2개여서 연패킹되어 각각의 변수안에 값이 들어간것
#만약에 li2 = [(1,2,3),(3,4),(5,6)]이렇게 되어있다면 첫번째 두번째 구문은 출력되지만 지금구문은 변수갯수가 맞지않아 출력되지 않음!
#타입이 문자열인 이유: f-string은 문자열 함수로 기존의 값이 숫자였어도 f-string으로 뽑았기때문에 자료형이 문자로 뽑힘

print()

#튜플의 언패킹
i,j = (1,2)
print(i,j) #변수 합쳐서 추출
print(i)
print(j)

#range()함수
#range(시작값, 끝값, 스텝)
#range(종료값) =>> range함수 안에 값1개라면 0(시작값 자동설정)부터 종료값까지
#스텝값이 음수라면 지정된 음수만큼 역순으로 출력
#스텝헷갈린다면 시작값에서 스텝수 만큼 더하거나 빼기!

print(range(1,10,2),type(range(1,10,2)))
#range()의 자료형으로 range가 출력되긴했으나 값이 출력되지 않음
#range의 값을 보고싶다면 반드시 **형변환**을 해주어야 함!

li1 = list(range(1,10,2))
print(li1,type(li1)) #자료형은 리스트로 나오고 range의 값이 나옴

tu1=tuple(range(10)) #튜플로 형변환하여 출력
print(tu1,type(tu1)) #종료값 하나만 적었기때문에 0~9까지 나옴

set1 = set(range(10,0,-1)) #역순으로 더 작은 숫자 출력하고싶으면 시작값이 항상 작을 수 밖에 없음!
print(set1,type(set1))

print()
for i in range(1,20,1):
  print(i) #for에서 바로 사용하는건 range를 집합으로 사용하기 때문

print()
for i in range(10,1,-2):
  print(i,end="")

print()

#반복횟수 지정할때 사용하는 range()
for i in range(5): #range에서 5라고적으면 0부터 1이 출력이 되는데 0,1,2,3,4 총5번 반복. 근데 변수를 출력하는게 아니라
#다른 걸 출력하게되므로 range안에 있는 집합이 다 끝날때까지 출력문에있는 문구를 반복출력해주는것!
  print("반가워! ")

for i in range(3):
  print("안녕!",end=" ")

#<for문 실습>
#for 문 사용하여 구구단 3단 만들기

#<로직구성>
#반복되어야하기때문에 for문사용
#3단이므로 3단은 고정값. 3이라는 고정값 변수 설정
#구구단이므로 range를 활용하여 3단안에 있는 숫자의 범위를 지정 1~9
#구구단이 시작된다는걸 알리는 의미로 맨위에 출력되도록 반복문 위에 문장출력

dan = 3
print("===3단 구구단 시작!===")
for i in range(1,10):
  print(f"{dan}x{i};{dan*i}")


#생각하면 좋은것들
#값에 고정값이 있는지 없는지 확인하기! 고정값이 있다면 변수로 만들어놓으면 편리함!
#반복츨력문에서 바로 원하는 결과 출력이 힘들다면 f-string이용하기!

#<실습2>
#1~10까지 숫자 합 구하기
#for문 사용
#출력결과가  "합: 55" 라고 나오도록 하기

#<로직구성>
#range로 1부터 10까지의 숫자 지정
#집합 값이 들어가있는 i변수는 기본으로 들어가야하고
#출력된 집합값이 어디엔가 저장이 되어있어야 다시 출력이 된 집합의 값과 계산이 가능하기때문에 출력된 집합의 값을 담아놓을 변수를 하나 만들기
#계속해서 반복해 값을 더해야하기때문에 +=복합 연산자 사용
#마지막 출력결과의 형태가 정해져있기때문에 for문 밖의 문장으로 출력


result = 0 #1로 시작하면 1+1로 시작됨!

for i in range(1,11):
  result+=i
print(f"합:{result}")

#여기서는 따로 더해주는것 하지 않음. 바로 합만 출력했음
#바로 결과만 보면 되기때문에 따로 i가 더해지지 않은 값을 보여줄 필요가 없기때문에 상관없지만 구구단의형식처럼 더해지는 과정을 보여주고싶다면
#이전값이 저장된 상태도 같이 보여주어야함

print()


#오답노트
result1 = 0

for i in range(0,11):
  result1+=i
  print(f"{result1}+{i}: {result1+i}")

#출력은 되나, 이전값 저장이 되지않음. i에 출력되는 그대로 그냥 result변수안에 들어가버려서 값이 달라짐. 즉 0부터 시작되어야하는데 그 0을 저장해놓을 값이 없고
#i가 더해지려고 할때 그 전값이 저장되는 변수가 없음
#코드는 순차출력됨   result1+=i이미 여기서 result의 값에 i값이 이미 더해져서 다시 변수안으로 들어간 작업까지 끝남.
#그 상태에서 print(result1+i)했기때문에 이미 윗줄에서 result는 1이 됐는데 출력문에서 다시 변수 i인 1과 더하니까 2가나오는 상태가 반복되는 상태가 되어 오답이 되는것!

print()

result = 0
for i in range(1,11):
  pre_re = result
  result+=i
  print(f"{pre_re}+{i}={pre_re+i}")
#최종적으로 더하는건 출력문에서 이전값과 반복되는 i값을 더했음!
#순차진행이기때문에 result+=i여기서 result의 값이 1이 되어도 아직 그 위의 문장인 pre_re여기서의 result값은 0임.
#덧셈을 하는 print()문도 반복문 안에 있기때문에 순차적으로 진행되어 나온 값끼리 더해서 이전값이 저장된 변수를 계속 사용할 수 있는것!

#이중반복문 / 중첩반복문
#반복문 안에 반복문을 한번 더 사용

for i in range(3): #바깥 for문
  for j in range(3): #안쪽 for문
    print(f"i:{i},j:{j}")

#각각 처음값인 0으로 출력한 후에 다시 반복하려고 올라가니 j반복문이 이미 있기때문에
#바깥쪽 반복문인 i로 가지 못하고 계속j반복문의 집합이 다끝날때까지 반복
#j반복문이 끝나고 i반복문으로 가서 1로 출력하려고 보니 안쪽 반복문이 바깥쪽 반복문의 영역안에 있기때문에
#다시 0부터 출력이 되고 이것이 바깥쪽 for문의 집합이 다 끝날때까지 반복하는것

#<이중 for문 실습>
#구구단 출력
#2~9단까지 출력, 이중for문 사용

#<로직구성>
#바깥쪽 for문은 2~9까지 출력되어야하고
#안쪽 for문 1~9까지 출력되어야함
#이중for문 사용예정이므로 굳이 고정값은 만들지 않음
#출력상태는 f-string을 이용할 예정


for i in range(2,10):
  print(f"===={i}단====")
  for j in range(1,10):
    print(f"{i}x{j}={i*j}")

#<개인실습>
#이중 for문 사용하여 숫자 타이틀 만들기
#10~110까지 각 앞자리에 맞는 숫자를 타이틀과 함께 출력할 예정

#<로직구성>
#바깥반복문은 안쪽반복문의 집합이 한바퀴 돌아야 끝난다는 점을 감안하여 바깥반복문의 반복실행문에 타이틀 출력
#안쪽반복문에는 계속 반복해서 출력이 되어야하는 결과값을 적어줌


for i in range(1,11): # 100까지 출력되어야 하기때문에 마지막이 10이 될 수 있도록 1,11로 집합범위 설정
  print(f"==숫자{i}단 시작==")
  for j in range(0,10): #1~9까지 반복 출력되어야하기때문에 1,10로 집합범위
    print(f"{i}{j}")
print(110) #110에서 멈추는건 반복문 자체에서는 불가능 하기때문에 for문과 상관없는 바깥문으로 출력

#<while이중 반복문>
#위와 같은 문제를 while문으로 풀어보기

num = list(range(1,11))
num1 =list(range(0,10))

while num<=10:
  print(num)
  while num<=9:
    print(f"{num}{num1}")

#기타 제어문
#1)break : 반복문 강제 종료언어

for i in range(1,11): #range를 사용하여 1~10까지 출력되어야하지만
  print(i)
  if i == 5: #조건문 if를 for문 안에 사용하여 i가 5라면
    break  #강제 종료하라는 명령어를 사용하여 5까지만 출력됨


print()

num = 10
while num==10: #정의된 변수가 계속10이기때문에 무한루프가 생성됨.
  print("숫자가 10입니다")
  break #하지만 print()문 밑에 강제 종료언어 break가 있기때문에 무한루프되지않고 출력문이 한번만 나오고 종료

#2)continue : 블록내의 처리를 건너뛰고 앞부분 위치로 돌아가서 다음 처리를 계속처리하는 구문. 바로다음순번의 loop실행

for i in range(1,11): #1~10까지 출력되어야하지만
  if i==5: #for문 안에 조건문 작성 i변수가 5라면
    continue #건너뛰어!
  print(i)
#조건문과 continue문도 for문 안에 있기때문에 집합에서 숫자가 추출될때마다
#if문에서 조건을 검사하고 조건문에 부합하지 않는다면 for문안에 포함된 출력문이 출력되어 그냥 변수값이 출력되는것

print()

#짝수 건너뛰고 홀수만 출력
for i in range(1,21):
  if i%2==0:
    continue
  print(i)

#3)pass문 : 실행할 코드가 없을때 다음 행동을 계속해서 진행하도록함

#pass문 사용하는 경우
#1)조건문에서 넣어줄 실행문이 딱히 없는경우
#2)calss선언할때, 초기값에 넣어줄 값이 없는 경우
#3)코드 작성 후 동작확인을 위해 해당 부분에서 오류가 발생하지 않도록 하기위해

if True:
  # print("조건문 출력") #if문에서 주석처리 됐을때 if문의 필수조건이라 에러남
  pass #근데 만약 조건문에 어떤 조건문을 적을지 결정하지 않았을 경우 pass를 적으면 위의 구문을 패스하고 마지막 구문이 출력되는것
print("프로그램 종료")


num =int(input("숫자를 입력하세요: "))

if num>=10:
  print("입력하신 숫자가 10이상입니다")
elif num>=5:
  # print("입력하신 숫자가 5이상, 10이하 입니다") #그냥 주석으로 처리하면 에러가 나지만
  pass #pass문이 있기때문에 에러나지 않고 프로그램 실행이 가능함
else:
  print("입력하신 숫자가 5이하입니다")
