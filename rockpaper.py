import random 
t = ["Rock", "Paper", "Scissors"]

computer = t[random.randint(0,2)]

contrinue_playing = True

while contrinue_playing: 
	print("Enter You option:")
	player = input("Rock, Paper, Scissors?\n")

	if(player == "Stop"):
		break
	if player == computer:
		print("Tie!")
	elif player == "Rock":
		if computer == "Paper":
			print("You lose!", computer, "covers", player)
		else:	
			print("You win!", player, "breaks", computer)
	elif player == "Paper":
		if computer == "Scissors":
			print("You lose!", computer, "cuts", player)
		else:
			print("You win!", player, "covers", computer)
	elif player == "Scissors":
		if computer == "Rock":
			print("You lose!", computer, "breaks", player)
		else: 
			print("You win!", player, "cuts", computer)
	else:
		print("Invalid input. Try Again!")

	player = False
	computer = t[random.randint(0,2)]
