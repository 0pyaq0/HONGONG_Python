# page 137, 문제 3
# 사용자에게 태어난 연도를 받아 띠를 출력하는 프로그램
# 작성 시 입력받은 연도를 12로 나눈 나머지를 사용
# 나머지가 0~11 일때 각각 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양띠 입니다.

 
str_input = input("태어난 해를 입력해 주세요> ")
birth_year = int(str_input) % 12

if birth_year == 0:
    print("원숭이 띠입니다.")
elif birth_year == 1:
    print("닭 띠입니다.")
elif birth_year == 2:
    print("개 띠입니다.")
elif birth_year == 3:
    print("돼지 띠입니다.")
elif birth_year == 4:
    print("쥐 띠입니다.")
elif birth_year == 5:
    print("소 띠입니다.")
elif birth_year == 6:
    print("범 띠입니다.")
elif birth_year == 7:
    print("토끼 띠입니다.")
elif birth_year == 8:
    print("용 띠입니다.")
elif birth_year == 9:
    print("뱀 띠입니다.")
elif birth_year == 10:
    print("말 띠입니다.")
elif birth_year == 11:
    print("양 띠입니다.")
