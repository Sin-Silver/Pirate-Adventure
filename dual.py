import random
import time
Player_HP = 100
Enemy_HP = 100

def attack(action):
	global Player_HP
	global Enemy_HP
	if action == "1":
		print("You both try and attack!")
		time.sleep(1)
		damage = random.randint(1,11) + 5
		Player_HP = Player_HP - damage
		print("The enemy hits you for",{damage},"Damage.")
		time.sleep(1)
		damage = random.randint(1,11) + 5
		Enemy_HP = Enemy_HP - damage
		print("You hit the enemy for",{damage},"Damage.")
		time.sleep(2)
	elif action == "2":
		print("You overcome your opponants attack with a massisive strike!")
		time.sleep(1)
		damage = random.randint(1,11) + 20
		Enemy_HP = Enemy_HP - damage
		print("You hit the enemy for",{damage},"Damage.")
		time.sleep(2)
	elif action == "3":
		print("You guard your opponents attack!")
		time.sleep(1)
		damage = random.randint(1,11)
		Player_HP = Player_HP - damage
		print("The enemy hits you for",{damage},"Damage.")
		time.sleep(2)
	else:
		print("you need to type 1, 2 or 3.")
		time.sleep(1)
		
def strike (action):
	global Player_HP
	global Enemy_HP
	if action == "1":
		print("Your opponant strikes you hard as you launch your attack!")
		time.sleep(1)
		damage = random.randint(1,11) + 20
		Player_HP = Player_HP - damage
		print("The enemy hits you for",{damage},"Damage.")
		time.sleep(2)
	elif action == "2":
		print("You both strike at each other, causing major damage!")
		time.sleep(1)
		damage = random.randint(1,11) + 10
		Player_HP = Player_HP - damage
		print("The enemy hits you for",{damage},"Damage.")
		time.sleep(1)
		damage = random.randint(1,11) + 10
		Enemy_HP = Enemy_HP - damage
		print("You hit the enemy for",{damage},"Damage.")
		time.sleep(2)
	elif action == "3":
		print("Your opponant lunches a vicious strike, but you manage to counter his deadly blow")
		time.sleep(1)
		damage = random.randint(1,11)+10
		Enemy_HP = Enemy_HP - damage
		print("You hit the enemy for",{damage},"Damage.")
		time.sleep(2)
	else:
		print("you need to type 1, 2 or 3.")
		
def counter (action):
	global Player_HP
	global Enemy_HP
	if action == "1":
		print("You carefully attack your guarded opponent.")
		time.sleep(1)
		damage = random.randint(1,11) + 10
		Enemy_HP = Enemy_HP - damage
		print("You hit the enemy for",{damage},"Damage")
		time.sleep(2)
	elif action == "2":
		print("You launch a powerful strike, only for your opponent to counter your blow!")
		time.sleep(1)
		damage = random.randint(1,11) + 10
		Player_HP = Enemy_HP - damage
		print("The enemy hits you for",{damage},"Damage")
		time.sleep(2)
	elif action == "3":
		print ("Both readying to counter, you and your oponent carefuly watch each other.")
		time.sleep(2)
	else:
		print("you need to type 1, 2 or 3.")
		
print ("You walk into the training field wearing clutching your blunted sword.\nStanding across from you standing across from you is your sword coach,\n impatiently tapping his feet")
wait = input()
print ("\"Took you long enough,\n This combat exerice is going to get you ready for what you face out there. Do you need an explination, or are you ready to begin? \"")
print ("Do you need an explination?")
answer = input("1.Yes\n2.No\n")

if answer == "1":
	print("Combat works on a roack paper scissor basis. Your three options are Attack, Strike and Counter. Attack beats Counter, Counter beats Strike and Strike beats Counter.")
	print("Strike is a powerful attack, using Strike whilst your oppnant Attacks will overwhelm them, inflicting heavy damage. If you laanch a Strike whislt your opponent Counters, they will turn the attack and hit you instead")
	print("If your opponent is readying a counter and you launch an Attack they won't be able to turn it, and will suffer minor damage")
	print("Watch your opponent carefully, and try to figure out what it is they are going to do, and act accordingly")
else:
	print ("Good lets begin!")

while Player_HP > 1 and Enemy_HP > 1:
	
		print ("Coach: I'm going to attack now, so strike me with everything you've got!")
		time.sleep(1)
		action = input("action?\n1.Attack\n2.Strike\n3.Counter\n>") #I need to make the player type 1,2, or 3.
		attack(action)
		print ("Your HP =", {Player_HP}, "opponant HP =", {Enemy_HP})
		time.sleep(1)
		print("Coach: I'm going to strike hard, so get ready to counter.")
		time.sleep(1)
		action = input("action?\n1.Attack\n2.Stike\n3.Counter\n>")
		strike(action)
		print ("Your HP =", {Player_HP}, "opponant HP =", {Enemy_HP})
		time.sleep(1)
		print("Coach: I'm going to get ready to counter, so attack me carefully.")
		time.sleep(1)
		action = input("action?\n1.Attack\n2.Strike\n3.Counter\n>")
		counter(action)
		
	
print ("Your HP =", {Player_HP}, "opponant HP =", {Enemy_HP})
if Player_HP > 1:
	print("you win")	
else:
	print("you loose")
