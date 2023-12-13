import random

print("\t\t\tWelcome to Blackjack!")

player_num = int(input("How many players? < 1 ~ 7 > : "))
player_num += 1 #딜러 인원수 추가

player_name = []
i = 0
while i < (player_num-1) : #추가한 딜러를 제외하고 이름 입력
    name = input("Enter player name : ")
    player_name.append(name)
    i += 1
player_name.append('dealer')

card = ['aH', '1H', '2H', '3H', '3H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'aD', '1D', '2D', '3D', '3D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'aS', '1S', '2S', '3S', '3S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'aC', '1C', '2C', '3C', '3C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']


player_card = [ ]
player_card_num = player_num * 2

j = 0
while j < player_card_num :   
    a = random.randint(0, 52)
    player_card.append(card[a])
    j += 1

k=0
while k < player_num :
    print(player_name[k] + " : " + player_card[i] + " "+ player_card[i+1])
    k += 1
    i += 2
    


