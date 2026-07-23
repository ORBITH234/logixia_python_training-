user_opinion = input("did nepa bring the light (y/n)? ").upper()

nepa_brought_light = user_opinion == "Y"

if not nepa_brought_light:
    print("Omo, go and turn on the Mikano generator!")
else:
    print("Up NEPA! Off the generator quickly make diesel no waste!")