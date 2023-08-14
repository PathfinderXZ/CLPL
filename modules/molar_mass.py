import re
import errors


def molar_mass(molecule: str):
    initializing_bracket = re.finditer(string=molecule, pattern="\(")
    ending_bracket = re.finditer(string=molecule, pattern="\)")
    initializing_bracket_position = []
    ending_bracket_position = []

    for i in initializing_bracket:
        initializing_bracket_position.append(i.span()[0])
    for i in ending_bracket:
        ending_bracket_position.append(i.span()[0])

    errors.errorCheck(initializing_bracket_position, ending_bracket_position)






molar_mass("P((N4))5()5")
