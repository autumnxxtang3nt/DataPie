

#CLASS TO DEFINE GREETINGS AND INTERACTIONS USED THROUGHOUT THE PROGRAM

class Greetings():
	def enter_host():
		print("ENTER HOSTNAME TO SCAN")
		host = input()

#STYLE DEFINING CLASS 

class Style():
	def RST():
		print("\033[0;0m")	
	def blink():
		print("\033[1;5m")
	class Colors():
		def C(str):
			print("\033[0;36m" + str)
		def M(str):
			print("\033[0;35m" + str)
		def RB(str):
			print("\033[1;31m" + str)
		def R(str):
			print("\033[0;31m" + str)
		def G(str):
			print("\033[0;32m" + str)
		def GB(str):
			print("\033[1;32m" + str)
		def BB(str):
			print("\033[1;34m" + str)