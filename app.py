import requests as request
import json

# check opponents
def opponents():

	# make a get request
	url = "https://umbelmania.umbel.com/opponents/"
	opponents = request.get(url)	

	# if status code okay
	if (opponents.status_code == 200):

		#for each oppoent print the opponent information
		for opponent in opponents.json():
			for key in opponent:

				print (key.ljust(13) + ":" + str(opponent[key]))

			print ("")
			print ("#"*30)
			print ("")

#check moves
def moves():

	#make a get request
	url = "https://umbelmania.umbel.com/moves/"
	moves = request.get(url)

	#create a dictionary of the moves
	dic = moves.json()

	#print each moves with details
	for key in dic:
		print("")
		print (key)
		print (dic[key])
		print("")

#re-write the moves for a specfic opponent
def write_moves(opponent): 

	#clear the file for the given opponent
	file = opponent + ".txt"
	print(file)
	open(file, "w").close()

	#make a post request for the specific opponent
	url  = "https://umbelmania.umbel.com/training/"
	headers = {'content-type': 'application/json'}
	payload = {"player_name" : "Herbie Fully Loaded", "opponent" : opponent}

	res = request.post(url, headers = headers, json = payload)
	match = res.json()

	#open the clean file for the opponent
	file = open(file, "w")

	#copy each move into file
	for move in range(1000):
		match["move"] = "K"

		attack = request.post(url, headers = headers, json = match)
		match = attack.json()
		opponentMove = match["gamestate"]["opponent_move"]
		print("Moves Remaining: " + str(match["gamestate"]["moves_remaining"]))
		file.write(opponentMove.upper() + "\n")
		# print("")

	file.close()

	print("Done getting moves!")


#find the right counter attack for specific moves
def findMove(move):
	counterAttack = "K"

	if (move == "D"):
		counterAttack = "C"

	elif (move == "C"): 
		counterAttack = "J"

	elif (move == "J"):
		counterAttack = "F"

	elif (move == "B"):
		counterAttack = "J"

	elif (move == "F"):
		counterAttack = "C"

	elif (move == "G"):
		counterAttack = "F"

	elif (move == "I"):
		counterAttack = "G"

	elif (move == "K"):
		counterAttack = "F"

	elif (move == "E"):
		counterAttack = "K"

	elif (move == "H"):
		counterAttack = "E"

	elif (move == "A"):
		counterAttack = "H"


	#return the right counter attack
	return counterAttack


#fighting.
def fight(opponent):

	# Fight in championship mode
	url  = "https://umbelmania.umbel.com/championship/"
	headers = {'content-type': 'application/json'}
	payload = {"player_name" : "Herbie Fully Loaded", "opponent" : opponent, "email" : "herbert.gutierrez@utexas.edu"}

	res = request.post(url, headers = headers, json = payload)
	match = res.json()

	print (match)
	fileName = opponent + ".txt"

	#open opponent file
	file = open(fileName, "r")

	#go through each move of the file for a counter attack
	for i in range(1000):
		line = file.readline().rstrip()
		counterAttack = findMove(line)
		match["move"] = counterAttack

		#send the request
		attack = request.post(url, headers = headers, json = match)

		#change the match
		match = attack.json()

		#print the results
		print("#"*20)
		print("score".ljust(15) + ":"+str(match["gamestate"]["score"]))
		print("totalScore".ljust(15) + ":"+ str(match["gamestate"]["total_score"]))
		print("oppenentMove".ljust(15) + ":"+ match["gamestate"]["opponent_move"])
		print("counterattack".ljust(15) + ":"+ counterAttack)

	#close the file
	file.close()


#main 
def main():

	# prompt user to see lucadores, see moves, fight luchador
	print ("#" * 70 )
	print("Select from the following options or press ENTER to quit")
	print()
	print("1: See Luchadores")
	print("2: See All Moves")
	print("3: Fight a Luchador")
	print("4: Re-write Moves")
	print()

	#user input
	start = str(input("Select option number or press ENTER to quit:"))
	print()

	#see opponents
	if (start == "1"):
		opponents()

	#see moves
	elif (start == "2"):
		moves()

	#fight a luchador
	elif (start == "3"):

		#select luchador to fight
		print("#" * 70)
		print()
		print("1: El Rey Muy Dante")
		print("2: Pato Bajo Jr.")
		print("3: Princesa Comico")
		print("4: Senor Amistoso")
		print()

		#user picked opponent
		opponent = str(input("Who would you like to fight? "))

		#fight the selected opponent
		if (opponent == "1"):
			fight("el-rey-muy-dante")
		elif (opponent == "2"):
			fight("pato-bajo-jr")
		elif (opponent == "3"):
			fight("princesa-comico")
		elif (opponent == "4"):
			fight("senor-amistoso")
		else:
			print ("wrong input")

	#re-write moves
	elif (start == "4"):

		#select luchador to rewrite moves for
		print("#" * 70)
		print()
		print("1: El Rey Muy Dante")
		print("2: Pato Bajo Jr.")
		print("3: Princesa Comico")
		print("4: Senor Amistoso")
		print()

		#user picked luchador
		opponent = str(input("Which luchador's counter attack moves would you like to rewrite? "))

		#rewrite selected opponent
		if (opponent == "1"):
			write_moves("el-rey-muy-dante")
		elif (opponent == "2"):
			write_moves("pato-bajo-jr")
		elif (opponent == "3"):
			write_moves("princesa-comico")
		elif (opponent == "4"):
			write_moves("senor-amistoso")
		else:
			print ("wrong input")

	#quitting program
	else:
		print("Good-bye!")


main()
# write_moves("el-rey-muy-dante")