import random

random_num = random.randint(1,100)
cnt = 1
max_cnt = 1

while(True):
  player_num = int(input())
  if(player_num < 1 or player_num > 100):
    print("please input number between 1 to 100")
    continue

  # 맞았을 때
  if(player_num == random_num):
    if(cnt > max_cnt):
      max_cnt = cnt
    print(f"correct! Your highest number of attempts is {max_cnt} times. more? y / n")
    answer = input()
    if(answer != 'y' and answer != 'n'):
      print("please input y or n")
      answer = input()
    if(answer == "y"):
      cnt = 0
      random_num = random.randint(1,100)
      print("new random number is created! Let's get it started")
      continue
    else:
      break
  # 입력한 수가 랜덤수보다 클 때
  elif(player_num > random_num):
    print("down")
    cnt += 1
    continue
  # 입력한 수가 랜덤수보다 작을 때
  else :
    cnt += 1
    print("up")
    continue