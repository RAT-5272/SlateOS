# Written by odinmedicbro, published by RAT-5272 on his behalf.
# ADADADADADDA

import time
profile = "new user"
password = "123"
passAttempts = 0
#commands
def lock():
	global passAttempts
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
	assurance = input("your current username is " + profile + " do you want to change it 1 = yes 2 = no: ")
	if assurance == "1":
		name = input("please enter username: ")
		yn = input("your new username is: " + name + " please answer 1 = yes 2 = no: ")
		if yn == "1":
			print("Your new username is " + name + " username will be updated.")
			profile = name
			settings()
		else:
			print("please try again")
			username()
	else:
		print("then your username will continue to be " + profile)
		settings()
def changePassword():
	global password
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
		construction("coin/dice")
		games()
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
		
lock()