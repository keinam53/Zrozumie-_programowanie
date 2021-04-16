#lista
smaki_lodow = ["malinowy",
    "truskawkowy",
    "czekoladowy",
    "pistacjowy",
    "kokosowy"]
#print("Smak lodów: ",smaki_lodow[1])
#print(f"Ilość elementów na liście: {len(smaki_lodow)}")
#print("Ostatni elemrnt listy: ",smaki_lodow[len(smaki_lodow)-1])
#print("Ostatni elemrnt listy: ",smaki_lodow[-2])
#print("Dwa najlepsze smaki: ", smaki_lodow[:2])
#print("Najgorsze smaki: ", smaki_lodow[2:])
smaki_lodow.append("kawowy")
smaki_lodow.insert(0, "jagodowy")
del smaki_lodow[4]
second_flavour= smaki_lodow.pop(1)
smaki_lodow.remove("czekoladowy")
smaki_lodow[-1] = "orzechowy"
print(second_flavour)
print(smaki_lodow)
