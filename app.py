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


#main 
def main():

	# opponents()
	# moves()

	url  = "https://umbelmania.umbel.com/training/"
	headers = {'content-type': 'application/json'}
	payload = {"player_name" : "Herbie Fully Loaded", "opponent" : "pato-bajo-jr"}
	match = request.post(url, headers = headers, json = payload)
	print (match.json())

	# print (moves.headers)
	# print (opponents.json())
	# print(len(opponents.json()))
	# print(opponents.status_code)
	# r = request.post("")


main()