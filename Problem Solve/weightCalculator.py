weight = int(input("Enter Your Weight: "))

command = input("What You Want to See your Weight? (K)g or (L)bs: ")
flag = True

if command.lower() == 'k':
    print("Your Weight in KG: " + str(weight * 0.453592))
elif command.lower() == 'l':
    print("Your Weight in LBS: " + str(weight / 0.453592))
else:
    print("Command Not Valid!")
    print("Please Inter K or L")
    flag = not flag

if flag:
    print("Thanks For Using")