# This is our first trial program
# By Tony
import random

while(True):
	random.seed()
	a = int(random.random() * 100)
	print("Please guess a number between 1 to 100:")
	b = int(input())
	if a == b: print("Yeah, you guessed right!")
	else: print("Nope, wrong guess. My number is actually: " + str(a))
	print("Do you want to continue? Y/N")
	ans = input()
	if (ans == 'n') or (ans == 'N') or (ans == "no") or (ans == "No") or (ans == "NO") or (ans == "Nope") or (ans == "nope"): break
	elif (ans == 'y') or (ans == 'Y') or (ans == "yes") or (ans == "Yes") or (ans == "YES") or (ans == "Yeah") or (ans == "yeah"): continue
print("Thanks for playing")
