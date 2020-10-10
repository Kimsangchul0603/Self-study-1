# 2.9 리스트

'''
1. 리스트는 순서가 있는 자료의 집합이다. 배열과 유사하지만 기능이 더 다양하다.
2. 그리고 리스트는 0번째부터 시작한다. 대괄호를 이용하여 인덱스에 맞는 값을 호출할 수 있다.
3. 리스트를 원하는 구간만 추출하는 slicing과 간격을 설정하여 분리할 수도 있다.
4. 리스트에 다른 리스트를 추가하고 싶으면 list.extend([])함수를 사용한다.
5. 리스트 내부 항목 존재 여부를 파악할 때는 (원소 in 리스트)를 사용한다.
6. 리스트에 항목을 추가할 때에는 list.append()를 사용한다.
'''

## 1번 예시
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_list = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)
list_sum = sum(integer_list)
# print(list_length) # 3
# print(list_sum) # 6, 리스트 원소가 숫자일 경우 연산이 가능한 듯
# print(list_of_list) # [[1, 2, 3], ['string', 0.1, True], []]
one = integer_list[0]
# print(one) # 1

################################################################

# 2.10 튜플

'''
1. 튜플은 변경할 수 없는 리스트이다. 따라서 수정을 제외한 모든 기능을 사용할 수 있다.
2. 괄호 혹은 아무런 기호 없이 사용한다.
3. 함수에서 여러 값을 반환할 때 튜플을 사용하면 편리하다.
4. 튜플과 리스트 모두 다중할당이 가능하다.
'''

## 2번 예시
my_list = [1, 2]
my_tuple = (3, 4)
other_tuple = 5, 6

# my_tuple[1] = 3, 튜플은 수정이 안되기 때문에 오류가 발생한다.

## 3번 예시
def sum_and_product(x, y):
    return (x+y), (x*y)

sp = sum_and_product(2, 3) 
# print(sp) # 5, 6
s, p = sum_and_product(5, 10)
# print(s, p) # 15, 50

## 4번 예시
x, y = 1, 2
x, y = y, x

################################################################

# 2.11 딕셔너리

'''
1. 딕셔너리는 또 다른 기본적인 데이터 구조이며, key와 value가 연결되어 있다.
2. 대괄호를 사용해서 키의 값을 불러올 수 있다.
3. 딕셔너리에 없는 키를 입력하면 KeyError가 발생한다.
   이를 dict.get()을 이용하여 키가 없는 경우 기본값을 반환할 수 있다.
   이미 키가 있는 경우는 값이 새롭게 변하지 않는다.
4. 여러 함수를 이용하여 모든 키를 한번에 살펴볼 수 있다.
5. 키는 수정할 수 없으며 리스트를 키로 사용할 수 없다. 
   다양한 키를 구성하려면 튜플이나 문자열을 이용한다. 
6. dict["키"] = value 를 이용하여 추가할 수 있다.
'''

## 1번 예시
grades = {"Joel": 80, "Tim": 95}
joel_grades = grades["Joel"]

# print(joel_grades) # 80

## 3번 예시
kate_grades = grades.get("Kate", 10)
# print(kate_grades) # 10

## 4번 예시
tweet = {
    "user" : "joelgrus",
    "text" : "Data science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["data", "#scinece", "#datascience"]
} # value가 많을 때는 리스트 형식으로 쓰는 듯

# print(tweet.keys()) # key만 출력
# print(tweet.values()) # value만 출력
# print(tweet.items()) # key와 value를 tuple로 묶어서 리스트로 출력

# 2.11.1 defaultdict

# 단어의 빈도수를 세는 딕셔너리 만들기 
document = []
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
    # word_counts 라는 새로운 딕셔너리를 만들어서 그 값을 1 추가하는 방법

'''
1. defaultdict을 이용하여 존재하지 않는 키를 자동으로 추가해줄 수 있다.
2. 이를 이용하려면 collections에서 모듈을 불러와야 한다. 
3. 리스트, 딕셔너리, 함수를 인자에 넣어줄 수 있다.
'''
from collections import defaultdict

word_counts = {}
for word in document:
    word_counts[word] += 1

# 이렇게 간단하게 작성할 수 있다.

## 3번 예시
dd_list = defaultdict(list)
dd_list[2].append(1) # dd_list는 {2:[1]} 포함
dd_dict = defaultdict(dict)
dd_dict["Joel"]["city"] = "Seattle" # {"Joel" : {"city": "Seattle"}} 생성