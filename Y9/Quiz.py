# Quiz
networkingQuestions = [
	"What port does HTTP use",
	"What port does HTTPS use",
	"True or False: UDP checks that the data was sent"
]
networkingAnswers = [
	"80",
	"443",
	"false"
]
linuxQuestions = [
	"Find kernel version",
	"Get ip address (old method)",
	"How to move a file?",
	"Who created linux",
	"Create an empty file with the name \"FooBar\" "
]
linuxAnswers = [
	"uname -a",
	"ifconfig",
	"mv",
	"Linus Torvalds",
	"touch FooBar"
]
def askQuestion(bank, increment):
	if bank == "networking":
		ask = input(networkingQuestions[increment] + ": ").lower()
		if ask == networkingAnswers[increment]:
			print("Correct")
		else:
			print("Incorrect")
	if bank == "linux":
		ask = input(linuxQuestions[increment] + ": ").lower()
		if ask == linuxAnswers[increment]:
			print("Correct")
		else:
			print("Incorrect")
print("\N{ESC}[33mWelcome to the computing quiz")

topic = input("""\N{ESC}[32mWhat topic?
\N{ESC}[35mA: Networking
B: Linux
""").lower()

		
if topic == "a":
	num = 0
	for i in range(len(networkingQuestions)):
		askQuestion("networking", num)
		num = num + 1
if topic == "b":
	num = 0
	for i in range(len(linuxQuestions)):
		askQuestion("linux", num)
		num = num + 1
	    
