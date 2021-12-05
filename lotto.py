import random
import time
print("Lotto numbers generator 1.0.\n")

try:
	rounds = int(input("How many rounds: "))
	print("\nGood Luck :)\n")
	for i in range(rounds):
		print("Round number[",i+1,"]\n")
		print("1. Number:",random.randint(1,49))
		print("2. Number:",random.randint(1,49))
		print("3. Number:",random.randint(1,49))
		print("4. Number:",random.randint(1,49))
		print("5. Number:",random.randint(1,49))
		print("6. Number:",random.randint(1,49))
		print("-------------")
		time.sleep(1)
except:
	print("\nBye :)")
