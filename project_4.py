score = 0

answer1 = input("what is the capital of france?")
if answer1.lower() == "paris":
    print("Correct!")
    score = score + 1

else:
    print("Wrong! The answer is Paris.")

answer2 = input("what is 5 + 7?")
if answer2 == "12":
    print("Correct!")
    score = score + 1

else:
    print("Wrong! The answer is 12.")

answer3 = input("What planet is known as the Red Planet?")
if answer3.lower() == "mars":
    print("Correct!")
    score = score + 1

else:
    print("Wrong! The answer is Mars.")

print("You scored", score, "out of 3")