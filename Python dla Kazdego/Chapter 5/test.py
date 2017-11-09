choices = ['strengh', 'wisdom', 'health', 'flex']
choice = int(input("\n\nWhat is your choice? ")) - 1
if choice < 4  or choice >= 0:
    attrib = choices[choice]
    print(attrib)
