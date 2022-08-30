# 실습 1-1
# 세 정수를 입력받아 최댓값 구하기

print("세 정수의 최댓값을 구합니다.")
a = int(input("정수 a의 값을 입력하세요.: "))
b = int(input("정수 b의 값을 입력하세요.: "))
c = int(input("정수 c의 값을 입력하세요.: "))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print("최댓값은 {maximum}입니다.".format(maximum = maximum))

#문제점: 비교하려는 값의 개수만큼 입력해줘야함, n-1번 비교해야함 O(n)
#해결방법: get_int 함수 정의 후 비교하려는 개수만큼 반복, 더 좋은 알고리즘 