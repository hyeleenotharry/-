import random

arr = ["rock", "scissor", "paper"]
num = random.randint(0,2)

result = [[0 for j in range(3)] for i in range(2)]

# ['win', 'draw', 'lose']
# [0, 0, 0]
result[0][0] = "win"
result[0][1] = "draw"
result[0][2] = "lose"

def print_arr(arr):
  print("your result : \n")
  for i in range(2):
    for j in range(3):
      print(f"{arr[i][j]} | ",end=" ")
    print("\n")
  print("\n")


while(True):
  player = input().lower()

  # 무승부
  if(arr[num] == player):
    print("draw")
    result[1][1] += 1

    print("continue? y / n")
    answer = input().lower()
    if(answer == 'y'):
      num = random.randint(0,2)
      continue
    else:
      print_arr(result)
      break
  # 플레이어가 가위를 냈을 대
  elif(player == "scissor"):
    if(arr[num] == "rock"):
      print("lose")
      result[1][2] += 1
      print_arr(result)
      print("continue? y / n")
      answer = input().lower()
      if(answer == 'y'):
        num = random.randint(0,2)
        continue
      else:
        print_arr(result)
        break
    else:
      print("win")
      result[1][0] += 1

      print("continue? y / n")
      answer = input().lower()
      if(answer == 'y'):
        num = random.randint(0,2)
        print('new game')
        continue
      else:
        print_arr(result)
        break
  # 플레이어가 바위를 냈을 때
  elif(player == "rock"):
    if(arr[num] == "paper"):
      print("lose")
      result[1][2] += 1

      print("continue? y / n")
      answer = input().lower()
      if(answer == 'y'):
        num = random.randint(0,2)
        continue
      else:
        print_arr(result)
        break
    else:
      print("win")
      result[1][0] += 1

      print("continue? y / n")
      answer = input().lower()
      if(answer == 'y'):
        num = random.randint(0,2)
        continue
      else:
        print_arr(result)
        break
  # 플레이어가 보를 냈을 때
  elif(player == "paper"):
    if(arr[num] == "scissor"):
      print("lose")
      result[1][2] += 1

      print("continue? y / n")
      answer = input().lower()
      if(answer == 'y'):
        num = random.randint(0,2)
        continue
      else:
        print_arr(result)
        break
    else:
      print("win")
      result[1][0] += 1
      print("continue? y / n")
      answer = input().lower()
      if(answer == 'y'):
        num = random.randint(0,2)
        continue
      else:
        print_arr(result)
        break
  else:
    print("please input right value")
    continue
