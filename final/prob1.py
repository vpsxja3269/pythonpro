test_str = input("문자열을 입력하시오. : ")

apl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sum = [0] * 52
leng = len(test_str)

h = 0
while h <= leng :
    for i in test_str:
        if i == apl[h]:
            sum[h] += 1
            h += 1
        else :
            sum[h] += 0
            h += 1

j = 0
while j <= 51 :
    print(apl[j]+" : "+ str(sum[j]))
    j += 1
