# 2.4 들여쓰기
'''
1. 파이썬은 중괄호 대신 들여쓰기를 사용한다. 이를 잘못하면 오류가 발생한다.
2. 공백문자는 소괄호와 대괄호 안에서 무시되기 때문에 끊어서 코딩이 가능하다.
   이때 역슬러시를 사용하면 다음줄로 이어지는 것을 명시할 수 있다. 
'''

## 2번 예시
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]] # 다음 줄은 들여쓰기와 큰 상관이 없어 보인다.
# print(list1)
# print(list2)

## 3번 예시
two_plus_three = 2 + \
                 3 # 이 3이라는 숫자또한 위치는 상관없다.
# print(two_plus_three)

################################################################

# 2.5 모듈
'''
1. 자연적으로 실행되지 않는 패키지 기능들을 import를 이용하여 모듈을 불러올 수 있다.
2. as를 이용하여 모듈의 별칭을 사용할 수 있다.
3. 모듈에서 몇몇 기능만 필요하다면 from import를 이용하여 골라올 수 있다.
'''

## 1번 예시
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)
# print(my_regex)

## 3번 예시
from collections import defaultdict, Counter
lookup = defaultdict(dict)
my_Counter = Counter()

################################################################

# 2.6 함수
'''
1. 함수는 0개 이상의 인자를 받아 결과를 반환하는 규칙이다. def를 이용하여 정의한다.
2. 짧은 익명의 람다 함수(lambda function)도 간편하게 만들 수 있다.
3. lambda 변수 : 함수식
4. 인자의 이름을 명시해줄 수도 있다. 인자 = "인자 이름"
   이 때 인자보다 적게 입력한다면 다른 인자 이름이 출력
'''
## 1번 예시
def appply_to_one(f):
       return f(1) # 인자가 1인 함수 f를 호출

def double(x):
       return x * 2

my_double = double
x = appply_to_one(my_double)
# print(x)

## 2번 예시
y = appply_to_one(lambda x: x+4)
# print(y)

## 4번 예시
def full_name(first = "성을 입력해라", last = "이름을 입력해라"):
       return first + " " + last

# print("내 이름은 : ", full_name("김", "상철")) # 김 상철
# print(full_name("김")) # 김 이름을 입력해라

################################################################

# 2.7 문자열

'''
1. 문자열은 작은 따옴표 또는 큰 따옴표를 묶어서 나타낸다.
2. 몇몇 특수 문자열을 인코딩할 때는 역슬래시("\")를 사용한다.
   역슬래시까지 문자로 표기하고 싶다면 문자열 앞에 r을 붙인다.
3. format을 이용하여 문자열을 합칠 수도 있다. 중괄호를 사용한다는 점이 특이
   f-string을 사용하면 더 편하다!
'''

## 2번 예시
tab_string = "\t"
# print(len(tab_string)) # 1
tab_string = r"\t"
# print(len(tab_string)) # 2

## 3번 예시
full_name = "{0} {1}".format("김", "상철") # format 함수
print(full_name) # 김 상철
first_name = "Kim"
last_name = "Sangchul"
full_name = f"{first_name} {last_name}" # f-string
print(full_name) # Kim sangchul

################################################################

# 2.8 예외처리

'''
1. 코드에 오류가 생기면 예외가 발생했음을 알려주어야 한다.
2. try와 except을 통해 예외처리를 한다.
'''

## 2번 예시

try:
   print(0/0)
except ZeroDivisionError:
   print("0으로 나눌 수 없습니다요")
