scores = []
while True :
  score = input("학생의 점수를 입력하세요:")
  if score.isdigit() :
    scores.append(int(score))
  else:
    break
print("입력 데이터 출력 : ", scores)
print("입력 데이터 출력 : ", sum(scores)/len(scores))
print("입력 데이터 출력 : ", len(scores))
