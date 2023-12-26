# 1264 모음의 개수

# 문제
# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

while True:
    s = input()
    if s == '#':
        break
    s = s.lower()
    cnt = 0
    for x in s : 
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x =='u':
            cnt += 1
    
    print(cnt)