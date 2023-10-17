import random

H_HP = random.randrange(50, 101)
M_HP = random.randrange(50, 101)
H_S = " "
M_S = " "
Count = 0

print("Hero HP : ", H_HP ,"Monster HP : ", M_HP)

while True :
    H_Attack = random.randrange(-10, 21)
    M_Attack = random.randrange(-10, 21)

    if H_Attack > 0 :
        H_S = "Succes"
        M_HP -= H_Attack
    
    else :
        H_S = "Fail"
    
    if M_Attack > 0 :
        M_S = "Success"
        H_HP -= M_Attack

    else :
            M_S = "Fail"

    print("Hero(HP : ", H_HP, ", Attack : ", H_Attack, " ) ", H_S, " <-> Monster(HP : ", M_HP, ", Attack : ", M_Attack, " ) ", M_S, sep=" ")
    Count += 1
    
    if H_HP < 0 or M_HP < 0 :
        break

print("---------------------------------------------------------------------")

print("Tetal phase : ", Count)

if M_HP > 0 :
     print("Monster Win")

else :
    print("Hero Win")