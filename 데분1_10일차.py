# -*- coding: utf-8 -*-
"""데분1_10일차.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PM9jntbp8_LonmP9iw-G58onhSEmu-6O
"""

#Family클래스
#데이터 속성 : adress(주소), name(이름)
#생성자 1개

class Family:
  def __init__(self,adress,name):
    self.adress=adress
    self.name=name

  def info(self):
    print(f"제이름은{self.name}이고 집주소는 {self.adress}입니다")

father = Family('서울','신영식') #아버지 주소 값 재정의 필요!
#짱구는 그대로 인천
son=Family('인천','짱구')

father.info()
son.info()

#데이터 속성확인
print(father.adress)
print(son.name)

#아버지의 주소가 서울로 바뀐다면?
#아버지의 주속값을 재정의 해주어야함
father.address='서울'
print(father.adress)

#클래스 변수와 인스턴스 변수
#한국사람을 나타내는 korean클래스 정의

class Korean:
  country='한국'
  #생성자
  def __init__(self,name,age,address):
    self.name=name
    self.age=age
    self.address=address

#클래스 변수: country
#인스턴스(객체변수) : name, age, address

#객체화

man1=Korean('정대만',25,'북산')
man2=Korean('이정환',25,'해남')

#객체(인스턴스 변수)
print(man1.name)
print(man1.age)
print(man1.address)

print(man2.name)
print(man2.age)
print(man2.address)

#클래스 변수
#클래스변수는 따로 self를 이용하지 않았는데도 객체별로 확인이 가능함
#객체가 모두 같은 값을 공유하고있기때문
#클래스변수는 객체와 같이 출력도 가능하고
print(man1.country)
print(man2.country)
#클래스명.클래스명 변수 방법으로도 호출이 가능하다(클래스 변수이기때문에)
print(Korean.country)
#하지만 객체(인스턴스)변수를 클래스명과 함께 호출할수없다
# print(Korean.name)이러면 에러발생
print(f"{man1.name}은 {man1.country}사람이다")
#클래스변수의 값이 변경되면 클래스변수를 공유하고있는 모든 객체의 값이 변경됨
#같은 변수를 공유하고있기때문!

#인스턴스 메소드
#인스턴스 메소드는 메소드 작성후 마지막에 self.매개변수명으로 정의한것을
#활용하여 했었것들을 메소드라고 함
#↓밑에 예시
  # def info(self):
  #   print(f"제이름은{self.name}이고 집주소는 {self.adress}입니다")

from types import ClassMethodDescriptorType
#클래스 메소드

class Korean:
  country='한국' #클래스변수
  @classmethod
  def trip(cls,country):
    if cls.country==country: #cls.country(Korean클래스의 클래스변수)==country(trip의 변수)
    #self대신 cls라는 것을 사용. cls는 클래스변수를 받아오는 기능.
      print('국내여행입니다')
    else:
      print("해외여행입니다")

Korean.trip('한국')
#클래스변수는 클래스명.메소드명/ 객체명.메소드명()으로사용



class band:
  band_type='락'
  @classmethod
  def band_sing(cls,type):
    if cls.band_type==type:
      print(f"장르는{type}입니다")
    else:
      print(f'락을 들으세요...')

band.band_sing('락')

class Band:
  band_tyep='락'
  @classmethod
  def band_sing(cls,type):
    if cls.band==type:
      print('락입니다')
    else:
      print(f'락을 들으세요..')

b1.band_type('락 ')

#정적메소드

class Korean:
  country='한국'
  @staticmethod
  def staticmethod(): #정적메소드는 self나 cls처럼 반드시 작성해줘야하는 매개변수가따로 없음
    return '정적메소드'
#매개변수가 없기때문에 return값이나 print()구문을 사용하여 이용가능
print(Korean.staticmethod())
#메소드를 실행시켰을때 정적메소드라는 반환값이 출력됨

#정적메소드

class Korean:
  country='한국'
  @staticmethod
  def staticmethod(name,age): #정적메소드는 self나 cls처럼 반드시 작성해줘야하는 매개변수가따로 없음
    print(name)
    print(age)
    return '정적메소드'

print(Korean.staticmethod('홍길동',25))
#매개변수를만들어주어도 가능.
#일반 사용자 정의함수 썼을때랑 방법이 동일
#밖에서 받아온 값들로만(매개변수) 값을 정의하는 경우에는 정적메소드를 사용하는것이 좋음
#객체를 만들지 않아도 이용가능하기때문

#일반 사용자 정의 함수처럼 정적메소드를 만들어 놓고 객체화시켜서 사용도 가능
p1=Korean
p1.name='홍길동'
p1.age=25
print(p1.name)
p1.country

print(f"{p1.name}은 {p1.age}살이며 {Korean.country}사람이다")

#상속

#<부모클래스 생성>
#부모 클래스의 생성자
class Person:
  def __init__(self,name):
    self.name=name
  #<부모 클래스의 메소드>
  def eat(self,food):
    print(f"{self.name}이/가 {food}를 먹습니다")
    #food는 인스턴스 매개변수가 아님. self가 붙은 name은 객체를 만들어서
    #이름값을 저장할 수있지만, food처럼 self를 지정하지 않는다면
    #food의 값은 특정한 객체에 저장되지 않으며 메소드를 호출 할때마다
    #food에 있는 값이 바뀔 수 있음

#자식 클래스 생성
class Student(Person):
  #자식클래스의 생성자
  def __init__(self,name,school):
    #자식클래스 생성할때 부모클래스의 매개변수에 name이 있기때문에
    #자식클래스 매개변수에도 name이 있어야함
    super().__init__(name)#부모클래스를 불러온다는 의미이므로 부모클래스에서
    #지정해준 매개변수들은 전부 순서까지 동일하게 적어야함
    #만약 부모테이블에서 def __init__(self,name,age,adderss)가 있었다면
    #super적을때 자식클래스에서도 전부다 순서에 맞게 적어야 한다는것!
    self.school=school
    #name은 부모에게서 상속받아온것이기때문에 따로 적지 않음. 이미 가지고 있기때문!

  def study(self):
    print(f"{self.name}은/는 {self.school}에서 공부합니다")


#<부모클래스의 속성>
#데이터 속성: name
#메소드: eat(생성자 제외)

#<자식클래스의 속성>
#데이터 속성: name(상속받은것), school(직접 추가)
#메소드: eat(상속받은것),study(직접 추가)

#부모클래스의 객체
pr1=Person('전신영')
pr1.eat('떡볶이')

#자식클래스의 객체
stud1=Student('해리포터','호그와트')
stud1.study()
stud1.eat('감자')#est메소드 정상실행. 자식클래스의 객체로 부모클래스의 메소드 사용
# pr1.study() 부모클래스가 자  식클래스의 메소드를 가질 수 없음

#부모 클래스의 인스턴스
print(isinstance(pr1,Person))
#isinstance(객체명, 클래스명) <-앞에 객체가 뒤에 클래스의 인스턴스냐고 묻는것

print(isinstance(pr1,Student)) #부모객체는 자식 클래스의 인스턴스가 될수없기에 False반환
print(isinstance(stud1,Person)) #자식객체는 부모 클래스의 인스턴스가 될 수 있음
print(isinstance(stud1,Student))

#오버라이딩
#자식클래스의 메소드가 부모클래스의 메소드를 다시 재정의해서 사용하는것을 의미

#부모클래스 Animal
#데이터 속성: 이름(name), 나이:(age)
#메소드 : 동물객체별 소리를 출력하는 메소드 : make_soud

class Animal:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def make_sound(self):
    pass #자식클래스에서 오버라이딩해서 사용할 것이기떄문에 pass

#Animal클래스를 상속받는 Dog클래스
#메소드 : 산책가자를 출력하는 메소드 :walk()

class Dog(Animal):
  def __init__(self,name,age):
    super().__init__(name,age)

  def walk(self):
    print(f"{self.name}이랑 산책가자!")

  #부모클래스의 메소드인 make_soud재정의
  def make_sound(self):
    print(f"{self.name}이가 멍멍!")

#Animal 클래스를 상속받는 Cat클래스
#메소드: 잘거야를 출력하는 메소드 : sleep

class Cat(Animal):
  def __init__(self,name,age):
    super().__init__(name,age)

  def sleep(self):
    print(f"{self.name}는 잘거야")

  def make_sound(self):
    print(f"{self.name}는 야옹!!")

#강아지, 고양이 객체생성후 매소드 호출

dog=Dog('멍멍이',3)
dog.make_sound()
dog.walk()
# dog.sleep()
#'Dog' object has no attribute 'sleep' 다른 자식 클래스에서 만든건 사용못함
print()

cat=Cat('고양이',4)
cat.sleep()
cat.make_sound()

#예외처리
#비정상적으로 프로그램이 종료되는것을 막고
#사용자에게 발생한 문제을 설명하기 위함

num1=3
num2=0
# print(num1/num2)
# ZeroDivisionError: division by zero  : 0으로 나누면 안된다는 오류
#0으로는 무언갈 나눌수가 없기때문에
print('출력끝')

if num2==0:
  print('0으로 나눌 수 없습니다')
else:
  print('num1/num2')

#보통 이런 오류는 조건문과 같은 다른 방법을 사용해서 오류 해결이 가능하지만
#매번 이런식으로 조건문과 다른 방법들을 이용해서 모든 오류를 처리할 수 없음
#그렇기 때문에 예외처리라는 것을 사용함

#예외처리

try:
  # try에는 예외가 발생될 것으로 예상되는 문장
  num1=int(input('첫번째 정수입력: '))
  num2=int(input('두번째 정수입력: '))
  print(f"{num1}/{num2}={round(num1/num2,2)}") #예외(오류)없이 정상실행되면 나올 문장
except ZeroDivisionError: #try블록안에서 ZeroDivisionError 오류가 발생했을때
  print("0으로 나눌 수 없습니다") #여기있는 문장을 실행시키겠다
except ValueError:
  print("정수만 입력할 수 있습니다")
except Exception:
  print('알수없는 예외가 발생했습니다')

#예외처리
#try~except~else~finally

li=['h','e','l','l','o']
print(li,type(li))
# print(li[100]) #인덱스 에러 발생
#IndexError: list index out of range

try:
  print(li[0])
  print(li[100])
except IndexError:
  print('범위에 맞는 인덱스를 입력하세요')
else:
  print(f"li리스트의 인덱스 범위는 {li[0]}입니다")
finally:
  print('프로그램 종료')

#예외강제 발생

num=int(input('1~5사이의 숫자를 입력하세요'))
#사실 그냥 문구로만 지정해준것이기때문에 5벗어나도 오류 안남
#근데 벗어났을때 오류를 내고 싶다면

if num>=5 or num<=1:
  raise ValueError('범위를 벗어났습니다.')

#<밴드소개서_상속class연습>

class Band:
  def __init__(self,name,member,song):
    self.name=name
    self.member=member
    self.song=song

  def band_info(self):
    print("===오늘의 밴드소개===")
    print(f"밴드명: {self.name}")
    print(f"멤버수: {self.member}명")
    print(f"참가곡: {self.song}")

  def cute(self,cute):
    print(f"{self.name}의 오늘 입덕멤은 {cute}입니다^^")
    print()

class Band_prize(Band):
  def __init__(self,name,member,song,prize):
    super().__init__(name,member,song)
    self.prize=prize

  def band_info(self): #오버라이딩
    super().band_info()
    print(f"수상갯수: {self.prize}개")

class Sing(Band):
  def __init__(self,name,member,song,sing):
    super().__init__(name,member,song)
    self.sing=sing

  def band_info(self,licys):
    super().band_info()
    print(f"오늘의 {self.sing}노래의 한줄 가사는 {licys}입니다! 오늘도 노래와 함께 모두 평안한 하루!")


#부모 클래스를 통해 각각 3가지의 밴드 소개서 만들기

b1=Band('유다빈 밴드',4,'항해')
b1.band_info()
b1.cute('유다빈')

bp=Band_prize('실리카겔',4,'루데자케이루',5)
bp.band_info()
bp.cute('김한주')

bs=Sing('롤링쿼츠',4,'빅토리','Fearlss')
bs.band_info('\'자 어때 기분이 별거 아니지? 이정돈 어림없지\'')
bs.cute('지영')