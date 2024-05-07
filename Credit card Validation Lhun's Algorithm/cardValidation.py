#Lhun's Algorithm
card = "5610591081018250"
num = list(card)

odd_sum = 0
even_sum = 0

for (idx,val) in enumerate(num):
    if idx%2 != 0:
        odd_sum = odd_sum + int(val)
    else:
        val = int(val)*2
        temp = val
        while(temp>0):
            digit = temp%10
            even_sum = even_sum + digit
            temp = temp//10

final_sum = odd_sum + even_sum

if final_sum%10 == 0:
    print("Valid Credit Card")
else:
    print("Not a Valid Credit Card")


