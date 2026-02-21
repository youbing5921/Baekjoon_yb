# '''
# 스택을 사용해서 진행 중이던 과제들을 임시 저장하게 함.
# (과제를 시간 순으로 정렬 필요)
# 1. 리스트에 있는 과제를 꺼냄.
# 2. 진행 중이던 과제가 있으면 스택에 넣고 방금 꺼낸 과제를 수행. (언제까지? 새로운 과제가 시작할 시각이 되기 전까지)
# 3. 과제를 미리 끝내면 스택에 넣어둔 멈춰둔 과제를 꺼내서 수행
# '''
# def solution(plans):
#     def add_time(start, playtime):
#         hour = int(start[0:2])
#         minute = int(start[3:]) + int(playtime)
#         if minute >= 60:
#             hour += minute // 60
#             minute %= 60
#         if hour < 10:
#             hour = "0"+str(hour)
#         else:
#             hour = str(hour)
#         return hour + ":" + str(minute)
    
#     def minus_time(start, end):
#         s_hour = int(start[0:2])
#         s_minute = int(start[3:])
#         e_hour = int(end[0:2])
#         e_minute = int(end[3:])
#         hour = e_hour - s_hour
#         minute = hour * 60 + e_minute - s_minute
#         return minute
    
#     answer = []
#     stack = []
    
#     # 과제 시간순 정렬(오름차순)
#     plans.sort(key=lambda x: x[1])
#     curr_time = plans[0][1]
    
#     for i, p in enumerate(plans):
#         name = p[0]
#         start = p[1]
#         playtime = p[2]
#         if i < len(plans) - 1: # 다음 과제가 있음.
#             next_time = plans[i+1][1]
#             if add_time(curr_time, playtime) <= next_time: # 다음 과제를 시작하기 전에 지금 과제를 끝낼 수 있음.
#                 curr_time = add_time(curr_time, playtime)
#                 answer.append(name)
                
#                 while stack: # 멈춰둔 과제하기
#                     sp = stack.pop()
#                     name = sp[0]
#                     start = sp[1]
#                     playtime = sp[2]
#                     if add_time(curr_time, playtime) <= next_time: # 멈춰둔 과제를 중간에 할 수 있음.
#                         curr_time = add_time(curr_time, playtime)
#                     else:
#                         stack.append(sp) # 롤백
#                         break
#             else: # 다음 과제 시작 전까지만 지금 과제하고 스택에 저장
#                 playtime = int(playtime)
#                 playtime -= minus_time(curr_time, next_time)
#                 playtime = str(playtime)
#                 stack.append([name, start, playtime])
#                 curr_time = next_time
#         else: # 다음 과제가 없음. 마지막 과제 + 스택에 있는 과제 하면 끝 
#             answer.append(name)
#             while stack:
#                 sp = stack.pop()
#                 answer.append(sp[0])
        
#     return answer

def solution(plans):
    def add_time(start, playtime):
        hour = int(start[0:2])
        minute = int(start[3:]) + playtime
        hour += minute // 60
        minute %= 60
        return f"{hour:02d}:{minute:02d}"
    
    def minus_time(start, end):
        s_hour = int(start[0:2])
        s_minute = int(start[3:])
        e_hour = int(end[0:2])
        e_minute = int(end[3:])
        return (e_hour - s_hour) * 60 + (e_minute - s_minute)
    
    answer = []
    stack = []
    
    plans.sort(key=lambda x: x[1])
    
    for i, p in enumerate(plans):
        name = p[0]
        start = p[1]
        playtime = int(p[2])
        
        curr_time = start  # ✅ 반드시 start 기준
        
        if i < len(plans) - 1:
            next_time = plans[i+1][1]
            remain = minus_time(curr_time, next_time)
            
            if playtime <= remain:
                answer.append(name)
                remain -= playtime
                curr_time = add_time(curr_time, playtime)
                
                # ✅ 남은 시간 동안 stack 처리
                while stack and remain > 0:
                    s_name, s_play = stack.pop()
                    if s_play <= remain:
                        remain -= s_play
                        answer.append(s_name)
                    else:
                        stack.append([s_name, s_play - remain])
                        break
            else:
                stack.append([name, playtime - remain])
        else:
            answer.append(name)
    
    while stack:
        answer.append(stack.pop()[0])
    
    return answer