import random
i = 0
count_of_person = 0
count_of_computer = 0
while i <= 5:
    i += 1
    a = ["rock", "paper", "scissor"]
    b = input("Enter what u want to play with machine---")
    c = random.choice(a)
    if b == c:
        print(c)
        print("The match is tie...")
    elif (b == a[0] and c == a[1]) or (b == a[1] and c == a[2]) or (b == a[2] and c == a[0]):
        print(c)
        print("U lose...")
        count_of_computer += 1
    elif (b == a[0] and c == a[2]) or (b == a[1] and c == a[0]) or (b == a[2] and c == a[1]):
        print(c)
        print("U win...")
        count_of_person += 1
    elif b != a[0] or b != a[1] or b != a[2]:
        print(c)
        print("Wrong output.......")

print("U won " + str(count_of_person) + " times.")
print("Computer won " + str(count_of_computer) + " times.")
if count_of_person > count_of_computer:
    print("U are the winner of this game.")
else:
    print("U lose this game.")
