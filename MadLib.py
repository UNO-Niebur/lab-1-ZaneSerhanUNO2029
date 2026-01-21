#MadLib.py
#Name:Zane Serhan
#Date:1/20/2026
#Assignment:Lab 1 MadLib
#Purpose: Create a madlib story by asking the user for words.

def main():
  print("Madlib")
  #Ask user for words
noun1=input("Enter a noun: ")
verb1=input("Enter a verb: ")
adjective1=input("Enter an adjective: ")
noun2=input("Enter another noun: ")
verb2=input("Enter another verb: ")
adjective2=input("Enter another adjective: ")

  #Print the story with the user supplied words.
print(f"Once upon a time, there was a {adjective2} {noun1} who loved to {verb1}.")
print(f"Every day, the {noun1} would {verb2} with a {adjective1} {noun2}.")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
