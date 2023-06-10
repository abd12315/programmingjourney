players=['Ahmed','Waqar','Rehman']
weapons=['hammer','sheild','long sword']
attack_points=[23,34,47]
print("Welcome to my game .... ")
char=input("The rules are simple first choose your character i.e Ahmed,Waqar,Rehman: ")
if char==players[0]:
    print(f"congraculations you have chosen {players[0]} Your weapon is {weapons[0]}")
if attack_points[0]>attack_points[1] and attack_points[0]>attack_points[2]:
    print(f"{players[0]} is the winner ")
elif char==players[1]:
    print(f"congraculations you have been chosen {players[1]} as your combatant with weapon {weapons[1]}")
if attack_points[1]>attack_points[0] and attack_points[1]>attack_points[2]:
    print(f"{players[1]} is the winner " )
elif char==players[2]:
    print(f"congraculation you've selected {players[2]} is as your character with {weapons[2]}")
if attack_points[2]>attack_points[1] and attack_points[2]>attack_points[0]:
    print(f"congraculatiion {players[2]} you've won")
else:
    print("Please rewrit your choices again and contac the developer for furthur questions ")
    
   


#do not write code under maintainece
