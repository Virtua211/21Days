import random

def play_game():
    options = ["石头", "剪刀", "布"]
    computer_choice = random.choice(options)
    user_choice = input("请出拳（石头、剪刀、布）: ")
    print("电脑出了: " + computer_choice)

    if user_choice == computer_choice:
        print("平局")
    elif (user_choice == "石头" and computer_choice == "剪刀") or (user_choice == "剪刀" and computer_choice == "布") or (user_choice == "布" and computer_choice == "石头"):
        print("你赢了")
    else:
        print("你输了")

play_game()
