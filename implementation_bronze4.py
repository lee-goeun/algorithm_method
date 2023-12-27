# 11720 숫자의 합
# 문제 : N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 깃 연결 확인

n = int(input())
m = input()

s = 0
for i in range(n):
    s += int(m[i])

print(s)