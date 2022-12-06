import random

game_win = 0
game_draw = 0
game_lose = 0
gamelist = ['가위', '바위', '보']
game_playtime = int(input('게임 할 횟수: '))


for i in range(game_playtime):
  game_random_index = random.randrange(0, 3)
  user_input = input()
  select_list_el = gamelist[game_random_index]

  
  if user_input == select_list_el:
    print('사용자: ',user_input ,'컴퓨터: ',select_list_el,'결과: 비겼다')
    game_draw = game_draw + 1

  elif user_input == '바위' and select_list_el == '가위':
    print('사용자: ',user_input ,'컴퓨터: ',select_list_el,'결과: 이겼다')
    game_win = game_win + 1
  elif user_input == '바위' and select_list_el == '보':
    print('사용자: ',user_input ,'컴퓨터: ',select_list_el,'결과: 졌다')
    game_lose = game_lose + 1
    
  elif user_input == '보' and select_list_el == '가위':
    print('사용자: ',user_input ,'컴퓨터: ',select_list_el,'결과: 졌다')
    game_lose = game_lose + 1
  elif user_input == '보' and select_list_el == '바위':
    print('사용자: ',user_input ,'컴퓨터: ',select_list_el,'결과: 이겼다')
    game_win = game_win + 1
    
  elif user_input == '가위' and select_list_el == '보':
    print('사용자: ',user_input ,'컴퓨터: ',select_list_el,'결과: 이겼다')
    game_win = game_win + 1
  elif user_input == '가위' and select_list_el == '바위':
    print('사용자: ',user_input ,'컴퓨터: ',select_list_el,'결과: 졌다')
    game_lose = game_lose + 1

print('[게임 통계]')
print('이긴 횟수: ',game_win)
print('진 횟수: ',game_lose)
print('비긴 횟수: ',game_draw)
game_result = ""
if game_win > game_lose:
  game_result = "이겼다"
elif game_win < game_lose:
  game_result = "졌다"
else:
  game_result = "<판단불가능>"
print('게임 결과 :',game_result)

