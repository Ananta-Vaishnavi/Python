import string
import random
rl = random.choice(string.ascii_letters)
rl=rl.lower()
print(rl)
a=int(input())
if a==(ord(rl)-96):
    print("Correct")
else:
    print(ord(rl)-96)
