s = input("Enter Your String: ")

flag = True

i = 0
j = len(s)-1
while i < j:
    if(s[i] != s[j]):
        flag = not flag
        break
    i += 1
    j -= 1
if flag:
    print("'" + s + "' String is Palimdrome")
else:
    print("'" + s + "' String is Not Palimdrome")

