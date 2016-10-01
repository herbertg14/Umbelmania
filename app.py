import requests as request
import json

# check opponents
def opponents():
	url = "https://umbelmania.umbel.com/opponents/"
	opponents = request.get(url)	

	if (opponents.status_code == 200):
		for opponent in opponents.json():
			for key in opponent:

				print (key.ljust(13) + ":" + str(opponent[key]))

			print ("")
			print ("#"*30)
			print ("")

#check moves
def moves():
	url = "https://umbelmania.umbel.com/moves/"

	moves = request.get(url)

	dic = moves.json()

	for key in dic:
		print("")
		print (key)
		print (dic[key])
		print("")

#re-write the moves for a specfic opponent
def write_moves(opponent): 

	file = opponent + ".txt"
	print(file)
	open(file, "w").close()

	url  = "https://umbelmania.umbel.com/training/"
	headers = {'content-type': 'application/json'}
	payload = {"player_name" : "Herbie Fully Loaded", "opponent" : opponent}

	res = request.post(url, headers = headers, json = payload)
	match = res.json()

	file = open(file, "w")

	for move in range(1000):
		match["move"] = "K"

		attack = request.post(url, headers = headers, json = match)
		match = attack.json()
		opponentMove = match["gamestate"]["opponent_move"]
		print(match["gamestate"]["moves_remaining"])
		file.write(opponentMove.upper() + "\n")
		print("")

	file.close()
	print(match)

#fighting Pato Bajo, Jr.
def fight_pato():

	url  = "https://umbelmania.umbel.com/training/"
	headers = {'content-type': 'application/json'}
	payload = {"player_name" : "Herbie Fully Loaded", "opponent" : "pato-bajo-jr"}

	res = request.post(url, headers = headers, json = payload)
	match = res.json()

	print(match)

	


	# for move in range(1000):
	# 	match["move"] = "K"

	# 	attack = request.post(url, headers = headers, json = match)
	# 	match = attack.json()
	# 	opponentMove = match["gamestate"]["opponent_move"]
	# 	print(opponentMove)
	# 	file.write(opponentMove.upper() + "\n")
	# 	print("")

	# file.close()
	# print(match)
#main 
def main():

	opponents()
	moves()
	# fight_pato()

	# write_moves("pato-bajo-jr")

	# r = open('PatoBajoJr.txt', "r")
	# for i in range(3):
	# 	line = r.readline().rstrip()
	# 	print(line)
	# print ("done")


	# res = request.post(url, headers = headers, json = payload)
	# match = res.json()
	# match["move"] = "K"
	# # print(match)
	# attack = request.post(url, headers = headers, json = match)
	# x = attack.json()
	# x["move"] = "K"
	# newPost = request.post(url, headers = headers, json = x)
	# print(newPost.json())
	# prin(attack.json())
	# print (res.json())

	# print (moves.headers)
	# print (opponents.json())
	# print(len(opponents.json()))
	# print(opponents.status_code)
	# r = request.post("")


main()