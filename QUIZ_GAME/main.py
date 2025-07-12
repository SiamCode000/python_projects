print("\nWelcome to the Quiz Game !")


user = input("\tDo you want to play the Game? ")
if(user.lower() == "yes"):
    print("Lets Go")
else:
    quit()

question_set1 = [
    ("1. What stands for ATM?", "automated telling machine"),
    ("2. Which following year Rabindranath Tagore borned?", "1861"),
    ("3. In which category Dr Yunus got Nobel Prize?", "peace"),
    ("4. Who was the first prime minister of Bangladesh?", "tajuddin ahmed"),
    ("5. In Which following year first world war held?", "1914"),
    ("6. What is the value of 'g' on Earth?", "9.8"),
    ("7. What is the exact name of Na (sodium)?", "natrium"),
    ("8. Who invented X-ray?", "rontgen"),
    ("9. Who is the father of Taxonomy?", "carolus linnaeus"),
    ("10. Who invented F = ma?", "newton")
]

score = 0

for q,a in question_set1:
    answer1 = input(q + " ")
    if(answer1.lower() == a):
        print("Correct !")
        score += 1
    else:
        print("Incorrect !")
    
Continue = input("\tDo you want to continue the Game? ")
if(Continue.lower() == "yes"):
    pass
else:
    print(f"You got {score} out of 10")
    quit()

question_set2 = [
    ("11. What is the capital of France?", "paris"),
    ("12. Who wrote 'Romeo and Juliet'?", "shakespeare"),
    ("13. What planet is known as the Red Planet?", "mars"),
    ("14. Who discovered gravity under an apple tree?", "newton"),
    ("15. What is the chemical symbol for water?", "h2o"),
    ("16. Who painted the Mona Lisa?", "da vinci"),
    ("17. What is 9 x 9?", "81"),
    ("18. In which continent is Egypt located?", "africa"),
    ("19. What gas do plants absorb from the air?", "carbon dioxide"),
    ("20. Who invented Python?", "guido van rossum")
]
for q,a in question_set2:
    answer2 = input(q + " ")
    if(answer2.lower() == a):
        print("Correct !")
        score += 1
    else:
        print("Incorrect !")

print(f"You got {score} out of 20")
if(score == [12,13,14,15,16,17,18,19,20]):
    print("\tGreat !")
else:
    print("\tNoob !!!")