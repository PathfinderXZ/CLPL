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

    bracket_map, bracket_count = [], 0
    for i in range(len(molecule)):
        if i in initializing_bracket_position:
            bracket_count += 1
        elif i in ending_bracket_position:
            bracket_count -= 1
        elif not (molecule[i].isnumeric()):
            bracket_map.append([i, bracket_count])

    print(initializing_bracket_position)
    print(ending_bracket_position)
    print(bracket_map)
    print(list(molecule))






molar_mass("P((N4))5(0)5")
