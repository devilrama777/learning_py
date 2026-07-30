'''
This is made by me
'''

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    if not isinstance(name, str) or name.isdigit():
        return "The character name should be a string"

    elif len(name) > 10:
        return "The character name is too long"

    elif len(name) == 0:
        return "The character should have a name"

    elif name.__contains__(' '):
        return "The character name should not contain spaces"

    stats = [strength ,intelligence ,charisma]

    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"

    elif any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"

    elif any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"

    elif sum(stats) != 7:
        return "The character should start with 7 points"

    stre = full_dot * int(strength) + empty_dot * (10 - int(strength))
    intel = full_dot *int(intelligence)+ empty_dot * (10 - int(intelligence))
    chari = full_dot * int(charisma) + empty_dot * (10 - int(charisma))
    return f"{name}\nSTR {stre}\nINT {intel}\nCHA {chari}"


print(create_character('ren', 4, 2, 1))