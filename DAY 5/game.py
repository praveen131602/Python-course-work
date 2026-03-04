moves = 15
winning_point = int(input("tell me the how many moves are required :"))
while moves >= 1:
     if 15-winning_point==moves:
        print("you won the game")
        break
     print(f"{moves} are left")
     moves -= 1
else:
    print("game over")
