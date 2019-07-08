room = 0
endding = "bad"
key = 0
ship = 0

print ("You are trapped in the brig of a pirate space ship. Suddenly, a massive expolision rocks the ship disabeling the containment field trapping you, you can hear fighting in the distance.\n You must escape.")
print ("Do you...")
print ("1. Escape down the corridor?")
print ("2. Climb down a hole made by the expolsion?")


path = input("> ")


if path == "1": # Rember the put the quotiation so it's string "1" not integer 1.
	print("You run down the corridor, but quickly hear foot steps approaching, what do you do?")
	print("1.Run away?")
	print("2.fight!")
	print("3.Hide!")
	
	path = input("> ")
	
	if path == "1":
		print("You run, but are quickly caught and killed!")
	elif path == "2":
		print("You are esily overpowered by the group of pirates and killed!")
		
	else:
		print("You hide down a small corridor, and notice a small vent. you climb down and follow crawl through a small tunnel")
		room = "1" # By setting room = '1' We can get the final scene to run when this chain ends
	
	
else:
	print ("You climb down the hole, which opens to a small, cramped tunnel.")
	print ("You can hear noise and fighting come from one direction, and the roar of fire from the other.")
	print ("Which way?\n 1.Head towards the fighting\n 2.Head away from the noise.")
	
	path = input("> ")
	
	if path == "2":
		print("You head down towards the sound of the fire. You are quitly crawling for a new minutes, when another explosion rips the ship apart and shoots you into space!")
	else:
		room = "1"
		
if room == "1":
	print("You climb down the tunnel, and eventually drop down into the ships hanger. The hanger bay is full of pirates fighting an invading alien force.")
	print("What do you do? \n1.Hide!\n2.Join in the fight.\n3.Try and steal a space ship.")
	 
	path = input("> ")
	 
	if path == "2":
		print ("You jump into the melee, but take a devastating blow to the head from a massive pirate.")
	elif path == "1":
		print ("You hide and wait for an oppertunity. Suddenly a metal orb with a blinking red light hits the wall behind you and lands by your feets.\n1. Oh shi... \n2. Pick it up and throw it!")
		
		path = input("> ")
		
		if path == "2":
			print("You pick up the ball and quickly throw it. Moments later it explodes, and you see pirates flying throught he sky! The head of an exploded pirate lands by your feet, a key card is wrapped around his neck, you take it.")
			ship = 1
			key = 1
	else: ship = 1

if ship == 1:
	print("Amongst all the fighting you make a dash for a near by space ship. You open the hatch and climb in, only to find the the controls locked!\nDo you...?")
	print("1.Shout and scream!\n2.Hack the terminal.")
	if key == 1:
		print("3.Use the keycard you picked up.")
	
	path = input("> ")
	
	if path == "1":
		print ("You bang the terminal with both fists in fustratation. The ship jerks, and it weapons systems come to life, launching it's nuclear payload into the small hanger.")
	elif path == "2":
		print("You use you mad hacking skills to override the console, bringing the ship to life!")
		endding = "good"
	elif path == "3":
		print("You use the key card to unlock the console, bringing the ship to life! ")
		endding = "good"

	
if endding == "good":
	print ("Amongst the fighting of the hangerbay, you pull the ship out, and you escape too open space!\n Well done!")
else:
	print("You died.\nTry again.")