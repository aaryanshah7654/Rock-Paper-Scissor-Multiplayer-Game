def gameWin(player_1,player_2):
    if player_1 == player_2:
        return None
    elif player_1 == 'r':
        if player_2 == 'p':
            return True
        elif player_2 == 's':
            return False
    elif player_1 == 'p':
        if player_2 == 's':
            return True
        elif player_2 == 'r':
            return False
    elif player_1 == 's':
        if player_2 == 'r':
            return True
        elif player_2 == 'p':
            return False
        
print("Welcome to Rock, Paper and Scissor Game")
player_1 = input("Player_1 : rock(r), paper(p) and scissor(s)?")
player_2 = input("Player_2 : rock(r), paper(p) and scissor(s)?")
print("Player 01 choose", player_1)
print("Player 02 choose", player_2)
a = gameWin(player_1,player_2)

if a == None:
    print("The game is a tie!")
elif a:
    print("player_2 Win")
else:
    print("player_1 Win") 