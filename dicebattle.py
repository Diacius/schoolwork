from dice import roll
attacker_points = 0
defender_points = 0
defender = roll('2d6')
attacker = roll('3d6')

print("Players' rolls")
print("Attacker:", attacker)
print("Defender:", defender)
attacker.sort()
defender.sort()
attacker =  attacker[::-1]
defender = defender[::-1]
print("Sorted")
print("Attacker:", attacker)
print("Defender:", defender)
if attacker[1] > defender[1]:
    print("Attackers highest roll was better attacker +1")
    attacker_points =+ 1
else :
    print("Attackers highest roll was better attacker +1")
    attacker_points =+ 1