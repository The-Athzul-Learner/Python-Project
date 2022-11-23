#If else syntax
myName=input("What is your name?")
if myName=="Atha":
  print("Welcome master, it's nice to see you here!")
else:
  print("You are not my master!")
  print("Please leave immediately or I will automaticaly call the police!")

print()

#Multiple if else with elif syntax
username=input("Username : ")
password=input("Password : ")
if username == "Atha" and password == "@r1sk@izul":
  print("Welcome Boss, Nice to meet you!")
elif username == "Nuzul" and password == "akuganteng":
  print("Welcome Master, It's happy to see you!")
elif username == "Harta" and password == "031104":
  print("Welcome Mr Hart, It's very nice to meet you!")
else :
  print("User is not recognized")
  print("\033[31m","Proceed to call authority")

print()

#Nesting if else
anime=input("Do you like anime?")
if anime == "yes":
  print("Wow, that's cool")
  animekind=input("What genre do you like?")
  if animekind=="romance":
    print("well... not cup of my tea")
  elif animekind=="action":
    print("My man, it's same to me!")
  elif animekind=="mecha":
    print("Ugh..are you still child..")
  else:
    print("Youre not really like anime, do you? ")
else:
  print("Oh I see,")



