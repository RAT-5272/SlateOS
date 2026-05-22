import random
import time
profile = "new user"
password = "123"
passAttempts = 0

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
		time.sleep(2)
		clearChat()
		print("""        _.-'~~`~~'-._
     .'`             `'.
    /                   \\
  /`       .-'~"-.       `\\
 ;        / `-    \\        ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \\ |        |
;        `~~;     \\        ;
 ;          /      \\)     ;
  \\        '.___.-'`"     /
   `\\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`
""")
		time.sleep(2)
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
		time.sleep(2)
		coin = random.randint(1, 2)
		if coin == 1:
			print("""        _.-'~~`~~'-._
3    /                   \\
  /`       .-'~"-.       `\\
 ;        / `-    \\        ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \\ |        |
;        `~~;     \\        ;
 ;          /      \\)     ;
  \\        '.___.-'`"     /
   `\\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`
""")
			print("you flipped heads")
			time.sleep(5)
			mainMenu()
		else:
			print("""             _.oood''''''''booo._
         _.o''      _____    * ''o._
       oP'  _.ooo''''   ''''o|o*_* 'Yo
     o8   oP                 | |'._* `8o
    d'  o8'_.--._            | |/  ,\\* `b
   d'  d'.' __   '.          | |: (( `\\
  8'  d'/,-'  `.   :         | |  ||\\_/* `8
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
			time.sleep(5)
			mainMenu()
	if CorD == "2":
		dice = random.randint(1, 6)
		print("you rolled a " + str(dice))
		time.sleep(5)
		mainMenu()
	if CorD == "3":
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
		construction("blackjack")
		games()
	if gamesChoice == "2":
		clearChat()
		construction("velkonian roulete")
		games()
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

#backjack()
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
lock()