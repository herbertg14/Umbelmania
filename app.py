import requests as request


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
		print (key)
		print (dic[key])


def main():


	# print (moves.headers)
	# print (opponents.json())
	# print(len(opponents.json()))
	# print(opponents.status_code)
	# r = request.post("")
	opponents()
	# moves()



main()