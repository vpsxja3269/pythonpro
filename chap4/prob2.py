import random

hero_hp = random.randrange(50,101)
monster_hp = random.randrange(50,101)



print("hero HP: ",hero_hp ,", monster HP:", monster_hp)

while hero_hp >  0 or monster_hp >  0:

    hero_att = random.randrange(-10,21)
    monster_att = random.randrange(-10,21)

    if monster_att > 0:
        hero_hp = hero_hp - monster_att
        A = 'success'

    else:
        A = 'fail'

    if hero_att > 0:
        monster_hp = monster_hp - hero_att 
        B = 'sussess'

    else:
        B = 'fail'

    print("hero(Hp:",hero_hp,", attack:",hero_att,") ",B,"  <-> monster(HP:",monster_hp,", attck:",monster_att,") ",A) 
