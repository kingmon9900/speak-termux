import os 
os.system("pkg i espeak")
while True:
  os.system("clear")
  x=input(" please enter text: ")
  os.system(f"espeak {x}")
