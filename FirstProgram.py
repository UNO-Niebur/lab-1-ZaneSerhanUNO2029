#FirstProgram.py
#Name:Zane Serhan
#Date:1/20/2025
#Assignment:LAB1
#Purpose: Write a simple program to greet and interact with user.

def main():
  print("First Program")
  #Say hello
print("Hello")
  #Ask for the user's name
name = input("What is your name?")
  #Use the user's name in the program.
print(f"Nice to meet you, {name}!")
  #Ask the user for their age.
age = int(input("How old are you?"))
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
birthyear = 2026 - age - 1
print(f"You were likely born in {birthyear}!")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()


