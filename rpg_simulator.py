import random

class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.attack = 10
        self.exp = 0
        self.weapon = "기본 검"

    def show_status(self):
        print("\n===== 상태창 =====")
        print(f"이름: {self.name}")
        print(f"레벨: {self.level}")
        print(f"HP: {self.hp}")
        print(f"공격력: {self.attack}")
        print(f"경험치: {self.exp}/100")
        print(f"장비: {self.weapon}")

    def hunt(self):
        monster = random.choice(["슬라임", "고블린", "늑대"])
        gained_exp = random.randint(15, 40)

        print(f"\n{monster} 처치!")
        print(f"경험치 +{gained_exp}")

        self.exp += gained_exp

        if self.exp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= 100
        self.hp += 20
        self.attack += 5

        print("\n★ 레벨 업! ★")
        print(f"현재 레벨: {self.level}")

    def equip_weapon(self):
        weapons = {
            "강철검": 5,
            "은검": 10,
            "전설의 검": 20
        }

        weapon = random.choice(list(weapons.keys()))

        self.weapon = weapon
        self.attack += weapons[weapon]

        print(f"\n{weapon} 획득!")
        print(f"공격력 +{weapons[weapon]}")


name = input("캐릭터 이름 입력: ")
player = Character(name)

while True:
    print("\n===== RPG 시뮬레이터 =====")
    print("1. 몬스터 사냥")
    print("2. 무기 뽑기")
    print("3. 상태창")
    print("4. 종료")

    choice = input("선택: ")

    if choice == "1":
        player.hunt()

    elif choice == "2":
        player.equip_weapon()

    elif choice == "3":
        player.show_status()

    elif choice == "4":
        print("게임 종료")
        break

    else:
        print("잘못된 입력입니다.")