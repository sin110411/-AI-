# -*- coding: utf-8 -*-
"""데분1_2일차 복습.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mFSmMFgX58pAsBxKC0MWunj6drx4N2RQ
"""

#형변환 함수
#1. 정수형 int(): 다른 자료형의 값을 정수형으로 변환한다.
#2. 실수형 float(): 다른 자료형의 값을 실수형으로 변환한다.
#3. 논리형 bool(): 다른 자료형의 값을 논리형으로 변환한다.
  #True : False를 제외한 모든값 참으로 변환
  #False : 0, 0.0, '',"",(),[],{}
#4.문자열 srt(): 다른 자료형의 값을 문자형으로 변환한다.

#정수형 변환함수 int

num1 = 12.1
print(num1,type(num1)) #실수로 나오며 type도 float

#int()함수 사용
print(int(num1),type(int(num1))) #정수 12로 출력되며 자료형도 int로 변환

age = 25.0
print(age,type(age))
print(int(age),type(int(age)))

#문자형 실수는 int()함수로 한번에 형변환 불가!
str_num1 = '10.1'
print(str_num1,type(str_num1)) #따옴표안에 들어가있기때문에 당연히 문자형으로 출력
# pritn(int(str_num1),type(int(str_num1)))
# 에러발생! 문자형 정수는 먼저 float함수를 사용하여 따옴표를 제거한 후 int로 변환가능

print(float(str_num1),type(float(str_num1))) #문자형 '10' =>> 10.0으로 실수형 숫자로변함
print(int(float(str_num1)),type(int(float(str_num1)))) #정수형 10으로 출력

#완전한 문자형은 int로 전환불가
# print(int('안녕'),type(int('안녕')))# 에러 발생. 적어도 숫자의형태여야함

#실수형 변환함수 float

num1= 314
print(num1,type(num1)) # 정수형이며 자료형도 int로 출력

#float() 함수 사용
print(float(num1),type(float(num1)))# 314.0인 실수로 출력되며 자료형도 float로 출력

평균 = 272
print(float(평균),type(float(평균)))

#논리형 실수변환
print(float(True),type(float(True))) #True는 1인데 1뒤에 0.0를 붙여서 1.0으로 변환
print(float(False),type(float(False))) #False는 0인데 뒤에 0.0붙여서 0.0으로 변환

#논리형 변환함수 bool()

print(True,type(True))  #논리형함수 출력
print(False,type(False))

# int()로 논리형함수 변환하기
print(int(True),type(int(True))) #참을 숫자변화하면 1
print(int(False),type(int(False))) #거짓을 숫자변환하면 0

#논리형 False
print(bool(''),type(bool(''))) #띄어쓰기조차 없는 값은 무조건 False 빈괄호도 마찬가지
print(bool(0),type(bool(0))) # 0도 마찬가지로 False변환

#논리형 True
print(bool(5),type(bool(5))) #0이 아닌 모든값은 True로 변환
print(bool(' '),type(bool(' '))) #논리형은 공백도 데이터로 인정하기때문에 True변환

#문자형 변환함수 str()
print(str(10),type(str(10))) #'10'이라는 문자형으로 변환
print(str(3.14),type(str(3.14))) # '3.14'라는 문자형으로 변환
print(str(True),type(str(True))) #'True'라는 문자형으로 변환

#시퀀스 자료형
print('안녕하세요')
#위와 같은 문자열은 문자들을 열거했다는 뜻으로 '안녕하세요'라는 문자형데이터가 아니라
#안, 녕, 하, 세, 요 5개의 데이터값이 묶여있는것
#이런 자료들을 시퀀스 자료형이라고 부름

#indexing : 특정문자열안에서 특정문자를 추출할때 사용하며 인덱스번호를 이용
#인덱스 번호: 문자열를 구성하는 모든 문자에 부여된 고유번호

#인덱스 시작: 0부터
#마이너스 인덱스의 시작번호: 뒤에서 -1

         #0,1,2,3,4
data1 = 'hello'
         #-5,-4,-3,-2,-1

#홀수번호만 가지고 오기
print(data1[1],data1[3]) # e,l출력
#짝수번호만 가지고 오기
print(data1[0],data1[2],data1[4]) # h l o 출력

#olleh역순 출력하기
print(data1[4]+data1[3]+data1[2]+data1[1]+data1[0]) #일반 인덱스번호 사용
print(data1[-1]+data1[-2]+data1[-3]+data1[-4]+data1[-5]) #마이너스 인덱스번호 사용


#<실습 적용_노래가사에서 특정 문자 추출하기>

no_pain = '내가만든 집에서 모두함께 노래를합시다'
#'내가만든+노래' 추출하기
print(no_pain[0]+no_pain[1]+no_pain[2]+no_pain[3],no_pain[14]+no_pain[15]) #일반인덱스 사용
print(no_pain[-20]+no_pain[-19]+no_pain[-18]+no_pain[-17],no_pain[-6]+no_pain[-5]) #마이너스 인덱스 사용

#한글자 가지고 오기
print(no_pain[4],type(no_pain)) #4번은 공백 추출. 공백도 인덱스 문자를 가지고 있으며 str자료형으로 추출
print(no_pain[-3],type(no_pain))

#슬라이싱(slicing
#문자열의 인덱스번호를 활용해서 한 문자 이상 구성된 단어나 문자를 추출할때 사용
#사용법: 변수명[시작값:끝값:스텝]
#*스텝은 필수는 아니며 미설정시 1로설정(건너뛰기 없이 한번에 출력)*

no_pain = '내가만든 집에서 모두함께 노래를합시다. 소외됐던 사람도 모두 함께 노래를 합시다'
print(no_pain,type(no_pain))

#슬라이싱하여 한문장만 출력하기
print(no_pain[0:19]) # 19번째인 '다'까지 입력했으나 '다'까지 나오지 않음. 끝자리에 입력된 숫자보다 하나를 덜 가져옴(입력된 값 바로 전까지)
print(no_pain[0:20]) #20번입력시 19번째까지 출력가능. 또한 스텝 미설정으로 건너뛰기없이 완전한 첫출 출력

#슬라이싱 스텝(step)
#한글자씩 건너뛰어서 출력하기
print(no_pain[0:44])# 전체 출력
print(no_pain[0:44:2]) #한글자씩 건너 뛰어서 출력

sing = 'no pain'
print(sing)
print(sing[::-1]) #맨처음, 맨끝값 생략한 후 음수로 스텝출력하면 역순으로 조회가능
print(no_pain[::-1])

#슬라이싱 처음과 끝
print(no_pain[::]) #맨처음과 끝값은 생략가능

#시퀀스 연산자

#문자열의 시퀀스 연산
# + : 문자열의 '연결'
data1 = 'hello'
data2 = 'python'
print(data1+data2)
# print(data1+10) #에러 발생
print(data1+'10') #'10은 문자이기때문에 가능'
print(data1+str(10)) #'str()'함수로 변형해주었기때문에 가능

# * : 문자열 반복
print(data1*3) #3번 반복출력
# print(data1*3.0) #3.0실수이기때문에 반복불가 에러
# print(data1*data2) #'hello'를 'python'만큼 곱해! <- 잘못된 명령문

#입력함수 : input()
#사용자로부터 값을 입력받기 위한 함수
#입력받은 값은 str로 저장되기때문에 다른 자료형으로 저장하고싶을때는 반드시 형변환 필수

band_name = '터치드'
print(band_name,type(band_name))

#input함수로 변경
band_name = input('좋아하는 밴드이름을 입력하세요: ')
print(band_name,type(band_name)) #입력된 값의 자료형을 알 수 있음
member =input('멤버 수는 몇명인가요?: ')
print(member,type(member)) #숫자임에도 불구하고 str로 입력됨

#<실습>
#변수와 input함수 사용해 순차적으로 등장하는 밴드설문조사지 만들기

band_name = input('가장 좋아하는 밴드이름을 입력하세요: ')
band_sing = input(band_name+"의 노래중 가장 가장 좋아하는 노래는?: ")
band_album = input(band_sing+"엘범을 구매하셨나요?: ")

print(band_name,type(band_name))
print(band_sing,type(band_sing))
print(band_album,type(band_album))

#순차적으로 출력되는 인터프리터 방식이기때문에 변수를 넣어 사용자가 입력한 값이 나옴

#입력함수 input()자료형 변환

num1 = int(input('숫자를 입력하세요:' ))
print(num1,type(num1))
#변수 만들때 input으로 감싸진 변수를 int함수로 한번더 감싸는 방식

num2 = float(input('소수점을 입력하세요: '))
print(num2,type(num2))
#실수로 값 받기

# num3 = input('숫자입력')
# print(int(숫자입력),type(숫자입력))
#에러! print문으로 받을때 값지정하게되면 입력칸까지는 등장하나, 입력하고나면 오류가남
#변수 만들때 input값을 무조건 원하는 자료형으로 나오도록 해야함

#이스케이스 문자
#문자열 안에서 특수한 기능을 하는 문자

#\n: 줄바꿈
#\': '작은 따옴표
#\": "큰 따옴표
#\\: \역슬래쉬 사용
#\t :tab키 사용(들여쓰기 / 일정간격 띄우기)키 표현

print('2일차 수업 복습중 입니다')
# print('2일차 수업 '복습중' 입니다') # 에러! 문자열''표식안에 또 ''표식을 썼기때문
print('2일차 수업 \'복습중\' 입니다') #복습 중 강조하여 출력가능

#문자열 표식 따옴표와 강조 따옴표가 다르다면 이스케이프문 사용안해도 가능
print('2일차 수업 "복습중"입니다')
print("2일차 수업 '복습중'입니다")

print("\t\'동해물\'과\n\"백두산\"")
#동해물 앞부분에 탭기적용해서 띄워줌. 동해물 이스케이프 작은 따옴표로 강조.
#백두산 큰따옴표로 바꾼후 줄바꿈을 해줌으로써 원래 한줄 출력이지만
#백두산이 밑으로 내려가서 출력됨



#<실습>
#이스케이프 문자를 사용하여 문장 한줄 형태 바꾸기

print("굉장히 졸리지만 복습내용은 끝내고 자야해") #기본 문장
print("굉장히\\ 졸리지만 \t\"복습내용\"은 \n끝내고 \'자야해\'")

#<실습2>
print("내가 만든집에서 모두함께 노래를 합시다") #기본 문장
print("내가\n 만든\"집\"에서\n \t모두함께\n \t노래를\n \t합시다")

#퍼센트연산자(형식지정자)
#%d : 정수 숫자
#%f : 실수 숫자
#%s : 문자형
#%s : 논리형

print("%d" %10)
print("%f" %3.14)
print("%.2f" %3.14) #퍼센트 뒤에 .N입력하면 입력한 숫자만큼의 자릿수만 보여줌
print("%s" %'python')
print("%s" %True)

print("%d %f %s" %(10, 15.5, '안녕')) #한꺼번에 사용시 괄호사용!

#str.format
#"{} {}".format(값1, 값2) #형식으로 사용

#10+20=30 표현하기
number1 = 10
number2 = 20
print(number1,"+",number2,"=",number1+number2) #기본 출력문활용

print("{}+{}={}".format(number1, number2, number1+number2))
print("{2}={1}+{0}".format(number1, number2, number1+number2))
print("{0}+{1}={2}".format(number1, number2, number1+number2))
