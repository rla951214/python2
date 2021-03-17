# for, while
# break, continue

# for문
# i = 첫번째인지 두번째인지 i라는 변수에 넣으라는 의미
# range(3) = 3번 반복하라는 의미
for i in range(3):
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야 그냥 있어")

# while문
i = 0
while i < 3:
  print(i) # 0
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야 그냥 있어")
  i = i + 1

i = 0
while True: # 무한루프
  print(i) # 0
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야 그냥 있어")
  i = i + 1

  if i > 2:
    break # 무한루프를 중지시키는 함수

# continue
for i in range(5):
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야 그냥 있어")

  continue # continue 아래는 실행이 되지않고
  # 루프의 첫번째 라인으로 돌아가는 함수

  print("정태: 안녕 철수와 영희야!")

