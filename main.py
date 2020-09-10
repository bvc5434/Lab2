# Author: Brendan Corso bvc5434@psu.edu
# Collaborator: JIULONG TANG jzt5526@psu.edu
# Collaborator: Mack Mason mjm8542@psu.edu
# Collaborator: Peter Schulman pks5481@psu.edu
# Section: 4
# Breakout: 6
lettergrade = "f"
def getLetterGrade(grade):
  if grade <= 100 and grade >= 93:
    return "A"
  elif grade < 93 and grade >= 90:
    return "A-"
  elif grade < 90 and grade >= 87:
    return "B+"
  elif grade < 87 and grade >= 83:
    return "B"
  elif grade < 83 and grade >= 80:
    return "B-"
  elif grade < 80 and grade >= 77:
    return "C+"
  elif grade < 77 and grade >= 70:
    return "C"
  elif grade < 70 and grade >= 60:
    return "D"
  else:
    return "F"
  print(f"Your letter grade for CMPSC 131 is {lettergrade}.\n")

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(grade)}.")

if __name__ == "__main__":
  run()