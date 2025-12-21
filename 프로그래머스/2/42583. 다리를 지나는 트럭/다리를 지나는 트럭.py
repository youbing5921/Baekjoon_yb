from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0 # 초
    d = deque([0] * bridge_length) # 다리
    n = len(truck_weights)
    i = 0 # truck_weights의 인덱스
    weight_sum = 0 # 다리에 올라간 무게 총합
    
    while i < n: # while문으로 수정 필요
        # 1초 동안 할 수 있는 일
        truck = truck_weights[i]
        # 다리에 있는 트럭을 1칸씩 이동시키기 == 다리에 있는 트럭을 내리기
        weight_sum -= d.popleft()
        # 다리에 트럭을 올리기 근데 무게 제한 길이 제한이 있어서 확인해야 함. 만약 트럭을 못 올리면 0을 추가하자
        if weight_sum + truck <= weight: # 트럭 올릴 수 있음.
            d.append(truck)
            weight_sum += truck
            i += 1
        else: # 트럭 못 올림. 대신 0 추가
            d.append(0)
        
        answer += 1 # 1초 지남.
    
    # 반복문은 마지막 트럭이 다리에 올라가는 순간 끝남. 그래서 마지막 트럭이 다리를 지나는 시간이 필요.
    return answer + bridge_length