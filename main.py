import random
import time
print("K = STONE")
print("N = SCISSOR")
print("B = PAPER")
print("HOW MANY WINS DO WE NEED TO WIN?")
howMany = int(input(""))
e = [0, 0]
print(1)
time.sleep(1)
print(2)
time.sleep(1)
print(3)
print("WRITE YOUR ITEM")
while True:
    d = ["K", "N", "B"]
    a = input("")
    b = random.randrange(0, 3)
    print(d[b])
    if a.lower() == "k" and d[b] == "N" or a.lower() == "n" and d[b] == "B" or a.lower() == "b" and d[b] == 'K':
        e[0] += 1
    elif d[b] == "K" and a.lower() == "n" or d[b] == "N" and a.lower() == "b" or d[b] == "B" and a.lower() == 'k':
        e[1] += 1
    print("ВЫ =", e[0])
    print("Я =", e[1])
    if e[1] == howMany or e[0] == howMany:
        break
