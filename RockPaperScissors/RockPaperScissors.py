import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("What do you choose ? Type 0 for rock , 1 for paper , and 2 for scissors.\n")
if choice == '0':
    print(f"rock\n{rock}")
elif choice == '1':
    print(f"paper\n{paper}")
elif choice == '2':
    print(f"scissors\n{scissors}")
else :
    print("Enter right number")

print("Computer chose:")
comp_choice = random.randint(0,2)
# print(comp_choice)
if comp_choice == 0:
    print(f"rock\n{rock}")
elif comp_choice == 1:
    print(f"paper\n{paper}")
elif comp_choice == 2:
    print(f"scissors\n{scissors}")

if (choice == '0' and comp_choice == 2) or (choice=='1'and comp_choice == 0) or (choice=='2'and comp_choice == 1):
    print("you win")
elif (choice == '0' and comp_choice == 0) or (choice=='1'and comp_choice == 1) or (choice=='2'and comp_choice == 2):
    print("It's a tie")
else:
    print("You lose")
