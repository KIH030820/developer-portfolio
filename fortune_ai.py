import random

fortunes = [
    "오늘은 새로운 도전을 시작하기 좋은 날입니다.",
    "계획했던 일을 마무리하기 좋은 날입니다.",
    "주변 사람과의 관계에서 좋은 일이 생길 수 있습니다.",
    "충동적인 결정은 피하는 것이 좋습니다.",
    "작은 기회가 큰 성공으로 이어질 수 있습니다.",
    "예상치 못한 행운이 찾아올 수 있습니다."
]

colors = [
    "빨강",
    "파랑",
    "노랑",
    "초록",
    "보라",
    "검정"
]

items = [
    "책",
    "이어폰",
    "커피",
    "노트북",
    "시계",
    "가방"
]

print("===== AI 운세 생성기 =====")

name = input("이름 입력: ")
mood = input("현재 기분 입력: ")

fortune = random.choice(fortunes)
color = random.choice(colors)
item = random.choice(items)
number = random.randint(1, 99)

print("\n======================")
print(f"{name}님의 오늘의 운세")
print("======================")
print(f"현재 기분: {mood}")
print()
print(f"운세: {fortune}")
print(f"행운의 숫자: {number}")
print(f"행운의 색상: {color}")
print(f"행운의 아이템: {item}")

if mood in ["피곤함", "졸림", "지침"]:
    print("\n오늘은 충분한 휴식도 중요합니다.")

elif mood in ["행복", "좋음", "신남"]:
    print("\n긍정적인 에너지가 좋은 결과를 가져올 수 있습니다.")

else:
    print("\n평소처럼 차분하게 하루를 보내보세요.")