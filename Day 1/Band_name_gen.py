# Band Name Generator

def band_name_gen():
	user_city = input("What's the name of the city you grew up in?\n").title()
	user_pet = input("What's the name of the your pet?\n").title()
	
	return f"Your band name could be {user_city} {user_pet}"
	

print(band_name_gen())
