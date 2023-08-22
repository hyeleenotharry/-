import re
import hashlib

# Member 클래스
class Member:
  name = ""
  username = ""
  password = 0000

  def __init__(self, name, username, password):
    self.name = name
    self.username = username
    # 비밀번호 sha256 방식으로 저장
    m = hashlib.sha256()
    self.password = m.update(password.encode('utf-8'))

  def display(self):
    print(f"회원님의 이름은 {self.name}, 아이디는 {self.username} 입니다.")

# Post 클래스
class Post:
  title = ""
  content = ""

  def __init__(self, title, content, author):
    self.title = title
    self.content = content
    self.author = author

  def display(self):
    print(f"{self.title}      {self.author}\n{self.content}\n")
    print("+++======================================================+++")

Lee = Member("Lee", "stella", 1111)
Kim = Member("Kim", "hello", 2222)
Park = Member("Park", "good", 3333)

# 리스트 선언
members = []
posts = []

members.append(Lee)
members.append(Kim)
members.append(Park)

for i in members:
  i.display()

# 포스트 내용 생성
for i in members:
  for j in range(3):
    if(i.name == "Lee"):
      posts.append(Post("안녕~", "내 이름은 '이'로 시작하고 아이디는 stella야", i.username))
    if(i.name == "Park"):
      posts.append(Post("안녕ㅋㅋ", "내 이름은 '박'으로 시작하고 아이디는 hello야", i.username))
    if(i.name == "Kim"):
      posts.append(Post("안녀엉", "내 이름은 '김'으로 시작하고 아이디는 good이야", i.username))

# 특정 사용자의 글만 보기
print("\n아이디 확인 : ")

for i in posts:
  if(i.author == "stella"):
    i.display()

# 특정 단어가 있는 내용의 제목만 보기
print("\n내용 확인 : \n")

for i in posts:
  if(i.content.find('으로') != -1):
    print(i.title)

print("\n")

# 멤버 생성
while(True):
  print("멤버를 생성하시겠습니까? y / n")
  answer = input()
  if(answer == 'y'):
    print("이름을 입력하세요 : ")
    new_name = input()
    print("아이디를 입력하세요 : ")
    new_username = input()
    print("비밀번호를 입력하세요 : ")
    new_password = int(input())
    members.append(Member(new_name, new_username, new_password))
    print("새로운 멤버가 생성되었습니다!")
    continue
  elif(answer == 'n'):
    for i in members:
      i.display()
    break
  else:
    print("y / n 중 하나만 입력해주세요")
    continue

print("\n")

# 포스트 생성
while(True):
  check = 0
  print("포스트를 입력하시겠습니까? y / n")
  answer = input()
  if(answer == 'y'):
    print("제목을 입력하세요 : ")
    new_title = input()
    print("내용을 입력하세요 : ")
    new_content = input()
    print("저자를 입력하세요 : ")
    new_author = input()
    for i in members:
      if(new_author == i.username):
        check += 1
    # username이 members에 존재하지 않을 시
    if(check == 0):
      print("존재하지 않는 사용자입니다. 올바른 사용자를 입력해주세요.")
      continue
    posts.append(Post(new_title, new_content, new_author))
    print("새로운 포스트가 생성되었습니다!")
    continue
  elif(answer == 'n'):
    for i in posts:
      i.display()
    break
  else:
    print("y / n 중 하나만 입력해주세요")
    continue
