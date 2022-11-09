print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's Play :)")
score = 0
answer = input("What does CPU Stand for? ").lower()
print(answer)
if answer == "central processing unit":
    print("correct")
    score +=1
else:
    print("Incorrect")

answer = input("What does RAM Stand for? ").lower()
if answer == "random access memory":
    print("correct")
    score +=1
else:
    print("Incorrect")

answer = input("What does HTML Stand for? ").lower()
if answer == "hyper text markup language":
    print("correct")
    score +=1
else:
    print("Incorrect")

answer = input("What does CSS Stand for? ").lower()
if answer == "cascading style sheets":
    print("correct")
    score +=1
else:
    print("Incorrect")

print(" You correct {} questions out of 4 ".format(score))