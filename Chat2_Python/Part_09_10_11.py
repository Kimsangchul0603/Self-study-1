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
'''

## 1번 예시
grades = {"Joel": 80, "Tim": 95}
joel_grades = grades["Joel"]
# print(joel_grades) # 80

## 3번 예시
kate_grades = grades.get("Kate", 10)
# print(kate_grades) # 10