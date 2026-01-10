# yellow가 i x j로 이뤄지고 그 겉을 brown이 감쌀 수 있는지 확인
# 1 <= i <= sqrt(yellow)
# math.isqrt(n) == floor(math.sqrt(n))
import math

def solution(brown, yellow):
    answer = []
    for i in range(1, 1 + math.isqrt(yellow)):
        if yellow % i == 0: # i가 yellow의 약수
            j = yellow // i
            bro = (i+2) * (j+2) - yellow
            if bro == brown: # 다 둘러쌀 수 있음
                return [j+2, i+2] # 가로가 길게 바꾸기
