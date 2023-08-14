import re
import errors
import data


def molar_mass(molecule: str):
    errors.errorCheck(len(molecule), 0, 1)

    molecule_origin_string = molecule

    molecule = molecule.replace("(", " ")
    molecule = molecule.replace(")", " ")
    molecule = molecule.replace("[", " ")
    molecule = molecule.replace("]", " ")


    molecule = list(molecule)

    position_counter, molecule_split = 0, []
    while not len(molecule)-2 <= position_counter:
        if molecule[position_counter].isupper() and molecule[position_counter+1].islower():
            molecule_split.append(molecule[position_counter]+molecule[position_counter+1])
            position_counter += 2
        else:
            molecule_split.append(molecule[position_counter])
            position_counter += 1
    else:
        if len(molecule) - position_counter == 2:
            if not molecule[-1].islower():
                molecule_split.append(molecule[-2])
                molecule_split.append(molecule[-1])
            else:
                molecule_split.append(molecule[-2] + molecule[-1])
        elif len(molecule) - position_counter == 1:
            molecule_split.append(molecule[-1])

    del position_counter

    print(molecule_origin_string)
    print(molecule)
    print(molecule_split)


molar_mass("CdO3Cu((Ni3))34")
