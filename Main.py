import random
import time
profile = "new user"
password = "123"
passAttempts = 0
chamberedRounds = 6


USER_DATA_FILE_PATH = "IfYouAreAHackerDontOpen.txt"

USER_DATA_LOOKUP_TABLE = [
	"Password",
	"Username"
]
USER_DATA_DEFAULTS = [
	"123",
	"None"
]

def ReadUserData(DataName):
	# Validate that the file exists in a bad way
	try:
		fil = open(USER_DATA_FILE_PATH, "x")
		fil.close()
	except:
		pass
	
	# Read file contents, if data not in file, return the default
	with open(USER_DATA_FILE_PATH, "r") as UserData:
		try:
			Information = UserData.readlines()[USER_DATA_LOOKUP_TABLE.index(DataName)]
		except:
			Information = USER_DATA_DEFAULTS[USER_DATA_LOOKUP_TABLE.index(DataName)]

	return Information.strip("\n")

def WriteUserData(DataName, Value):
	# Validate that the file exists in a bad way
	try:
		fil = open(USER_DATA_FILE_PATH, "x")
		fil.close()
	except:
		pass

	# Read data from the file
	Index = USER_DATA_LOOKUP_TABLE.index(DataName)
	with open(USER_DATA_FILE_PATH, "r") as UserData:
		UserDataContentsADAD = UserData.readlines()

		UserDataContents = []
		for Content in UserDataContentsADAD:
			UserDataContents.append(Content.strip("\n"))

	
	try:
		CurrentValue = UserDataContents[Index]
	except:
		for i in range(len(UserDataContents), Index+1):
			UserDataContents.append(USER_DATA_DEFAULTS[i])
	
	UserDataContents[Index] = Value

	with open(USER_DATA_FILE_PATH, "w") as UserData:
		UserData.write("\n".join(UserDataContents))

#commands

def deck():
	hearts = "♥"
	diamonds = "♦"
	clubs = "♣"
	spades = "♠"
	suit = [hearts, diamonds, clubs, spades]
	rank = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
	value = [2,3,4,5,6,7,8,9,10,10,10,10,11]
	#here till next comment is vibe coded and will be changed
	card = random.randint(0, 51)
	cardsuit = suit[card//13]
	cardrank = rank[card%13]
	cardvalue = value[card%13]
	#end of vibe code
	print("your card is the " + cardrank + " of " + cardsuit + " with a value of " + str(cardvalue))
	time.sleep(5)
	mainMenu()
def velkonianRoulete():
	global chamberedRounds
	learn = input("welcome to velkonian roulete the rules are simple do you want to learn how to play 1 = yes 2 = no: ")
	if learn == "1":
		print("1) there is a pistol with 6 chambers and 6 bullets 1 is live 5 are blanks")
		print("2) The game you play is bullshit")
		print("3) if you lose you spin the chamber and fire towards yourself")
		print("4) if you win the opponent spins the chamber and fire towards themselves")
		print("5) if you get the live round you lose and the game ends and if you get a blank the game carries on")
		input("Press enter once you have read and understood this ^")
		clearChat()
		bsRules = input("do you want to learn how to play bullshit 1 = yes 2 = no: ")
		if bsRules == "1":
			print("1) each player is dealt 5 cards")
			print("2) each turn a player plays a card face down and says what card it is")
			print("3) you are allowed to lie about what card you play or tell the truth")
			print("4) the next player must then play a card of the same or higher value or call bullshit")
			print("5) if you call bullshit and the player was lying you win but if they were telling the truth you lose")
			print("6) the player with the highest card discards the card they played the players with lower cards keep their cards")
			print("7) the first player to get rid of all their cards wins and all other players lose")
			print("8) if the live round is fired the game ends even if there are cards left")
			print("9) if multiple players have lost at the end of the game the player with the most cards is the one who loses \n   and must fire the gun")
			input("Press enter once you have read and understood this ^")
			clearChat()
		else:
			clearChat()
			mainMenu()
	else:
		clearChat()
		mainMenu()

def diceCoins():
	CorD = input("do you want to flip a coin or roll a dice 1 = coin 2 = dice if u want to exit exit = 3: ")
	if CorD == "1":
		print("""                ______________
    __,.,---'''''           ;   '''''---..._
 ,-'         :::::::::   : ;;             '`-.
'              ,,,::::     ''    ::   ::::    ;
|            ::'''       :::::::::::::::::     ;
|'-.._     ::::::::::   ::::      ::       __,,
 '-.._''`---.....______________.....---''__,,-
      ''`---.....______________.....---''
""") 
		time.sleep(0.5)
		clearChat()
		print("""        _.-'~~`~~'-._
     .'`             `'.
    /                   |
  /`       .-'~"-.       `|
 ;        / `-    \        ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \\ |        |
;        `~~;     \\        ;
 ;          /      \\)     ;
  \        '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`
""")
		time.sleep(0.5)
		clearChat()
		print("""                ______________
    __,.,---'''''           ;   '''''---..._
 ,-'         :::::::::   : ;;             '`-.
'              ,,,::::     ''    ::   ::::    ;
|            ::'''       :::::::::::::::::     ;
|'-.._     ::::::::::   ::::      ::       __,,
 '-.._''`---.....______________.....---''__,,-
      ''`---.....______________.....---''
""")
		
		time.sleep(0.5)
		clearChat()
		print("""        _.-'~~`~~'-._
     .'`             `'.
    /                   |
  /`       .-'~"-.       `|
 ;        / `-    \        ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \\ |        |
;        `~~;     \\        ;
 ;          /      \\)     ;
  \        '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`
""")
		time.sleep(0.5)
		clearChat()
		print("""                ______________
    __,.,---'''''           ;   '''''---..._
 ,-'         :::::::::   : ;;             '`-.
'              ,,,::::     ''    ::   ::::    ;
|            ::'''       :::::::::::::::::     ;
|'-.._     ::::::::::   ::::      ::       __,,
 '-.._''`---.....______________.....---''__,,-
      ''`---.....______________.....---''
""") 
		time.sleep(0.5)
		clearChat()
		coin = random.randint(1, 2)
		if coin == 1:
			print("""        _.-'~~`~~'-._
     .'`             `'.
    /                   |
  /`       .-'~"-.       `|
 ;        / `-    \        ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \\ |        |
;        `~~;     \\        ;
 ;          /      \\)     ;
  \        '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`
""")
			print("you flipped heads")
			time.sleep(5)
			clearChat()
			mainMenu()
		else:
			print("""             _.oood''''''''booo._
         _.o''      _____    * ''o._
       oP'  _.ooo''''   ''''o|o*_* 'Yo
     o8   oP                 | |'._* `8o
    d'  o8'_.--._            | |/  ,\* `b
   d'  d'.' __   '.          | |: (( `\
  8'  d'/,-'  `.   :         | |  ||\_/* `8
 8   8'|/      :   :    |)   _ |  || |`|   8
,8  8          :  :   /)| \\ || |\\_|| | |8  8.
8' ,8         /  :    " /_) |`:' | | | |8. `8
8  8'        /  /       _ _='  \\ ' __   __  8
8  8        /  /        \\|__ |  | |  | | 8| 8
8  8.      /  /         ||   |  | |-:' | 8| 8
8. `8    ,' ,'       __/ |__ |__| |  \\ |__|,8
`8  8  ,' ,'      _ /     __ . . . . . .8LL8'
 8   8'   `------'/(    ,'  `.`. | | ,-|8  8
  8.(_________dd_/  \\__/ '  0|`.`: |: (8 ,8
   Y.  Y.                    | :/| |,\\|* .P
    Y.  '8.          .,o     | | |,|;'*  ,P
     '8.  'Yo_               | |p|'* ,8'
       'Y_   `'ooo.__   __.oo|'* * _P'
         `''oo_     '''''    * _oo''
              `'''boooooood'''
""")
			print("you flipped tails")
			input("Press enter to continue.")
			clearChat()
			mainMenu()
	if CorD == "2":
		dice = random.randint(1, 6)
		print("you rolled a " + str(dice))
		input("Press enter to continue.")
		mainMenu()
	if CorD == "3":
		clearChat()
		mainMenu()
def lock():
	global passAttempts, password
	if passAttempts == 5:
		print("device will now be locked for 2 mins")
		for i in range (1, 120):
			clearChat()
			time.sleep(1)
			print(i)
			clearChat()
			passAttempts = 3
	else:
		print("""  .---.
 /    |\\________________
( ()  | ________   _   _)
 \\    |/        | | | |
  `---'         "-" |_|
							

""")
	
	password = ReadUserData("Password")

	enterAttempt = input("please enter password to enter device: ")
	if enterAttempt == password:
		clearChat()
		mainMenu()
	else:
		print("wrong password")
		passAttempts = passAttempts + 1
		lock()
	
def mainMenu():
	mainMenuOption = input(f"---- welcome {profile} ---- \n{'-'*len('-------- welcome  ')}{'-'*len(profile)} \n 1) Settings \n 2) Messages \n 3) Time/Calendar \n 4) Games \n")
	if mainMenuOption == "1":
		clearChat()
		settings()
	if mainMenuOption == "2":
		clearChat()
		construction("Messages")
		mainMenu()
	if mainMenuOption == "3":
		clearChat()
		construction("Time/Calendar")
		mainMenu()
	if mainMenuOption == "4":
		clearChat()
		games()
def clearChat():
	print("\n"*50)
def wipeChat():
	print("\n"*150)  
def construction(FeatureName = "Unnamed"):
	print(f"""The feature '{FeatureName}' is not currently available

8b,dPPYba,   ,adPPYba,   
88P'   `"8a a8"     "8a  
88       88 8b       d8  
88       88 "8a,   ,a8"  
88       88  `"YbbdP"'   
                         """)


def username():
	global profile

	profile = ReadUserData("Username")

	assurance = input("your current username is " + profile + " do you want to change it 1 = yes 2 = no: ")
	if assurance == "1":
		name = input("please enter username: ")
		yn = input("your new username is: " + name + " please answer 1 = yes 2 = no: ")
		if yn == "1":
			print("Your new username is " + name + " username will be updated.")
			profile = name
			WriteUserData("Username", profile)
			settings()
		else:
			print("please try again")
			username()
	else:
		print("then your username will continue to be " + profile)
		settings()
def changePassword():
	global password

	password = ReadUserData("Password")

	if password == "123":
		print("Your password is currently the default, '123'.")

	passChange = input("do you want to change your password 1 = yes 2 = no: ")
	if passChange == "1":
		passlock = input("to change password please enter current password: ")
		if passlock == password:
			print("password correct you may now change your password")
			newpassword = input("please enter password: ")
			newpassword2 = input("please enter password again: ")
			if newpassword == newpassword2:
				password = newpassword
				print("password now changed your new password is " + password)
				WriteUserData("Password", password)
				settings()
			else:
				print("sorry these do not match please try again")
				changePassword()
		else:
			print("sorry the password is wrong please try again")
			changePassword()
	else:
		settings()
def games():
	gamesChoice = input("-------GAMES------- \n------------------- \n 1) blackjack \n 2) velkonian roulete \n 3) coin/dice \n 4) tank battles \n 5) back \n")
	if gamesChoice == "1":
		clearChat()
		deck()
	if gamesChoice == "2":
		clearChat()
		velkonianRoulete()
	if gamesChoice == "3":
		clearChat()
		diceCoins()
	if gamesChoice == "5":
		clearChat()
		mainMenu()
	if gamesChoice == "4":
		clearChat()
		construction("tank battles")
		games()

def settings():
	settingChoice = input("----SETTINGS---- \n---------------- \n 1) account \n 2) password \n 3) clean slate \n 4) back to home \n 5) lock device \n")
	if settingChoice == "1":
		username()
	if settingChoice == "2":
		changePassword()
	if settingChoice == "3":
		clearChat()
		construction("Clean Slate")
		settings()
	if settingChoice == "4":
		clearChat()
		mainMenu()
	if settingChoice == "5":
		lockyn = input("are you sure you want to lock this device 1 = yes 2 = no: ")
		if lockyn == "1":
			wipeChat()
			wipeChat()
			lock()
		else:
			clearChat()
			settings()
		
profile = ReadUserData("Username")
password = ReadUserData("Password")
clearChat()
lock()