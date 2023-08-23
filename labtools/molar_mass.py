import data
import errors
import copy


def mol_mass(molecule: str):
    errors.error_check(len(molecule), 0, 1)
    
    if molecule in list(data.compounds.keys()):
        return data.compounds[molecule]
    
    for group in list(data.groups.keys()):
        if group in molecule:
            molecule = molecule.replace(group, data.groups[group])

    def numeric_check(string: str, pos_counter: int):
        number = str(string[pos_counter])
        try:
            while string[pos_counter + 1].isnumeric():
                number += string[pos_counter + 1]
                pos_counter += 1
        except IndexError:
            return int(number), pos_counter + 1
        return int(number), pos_counter + 1

    molecule = molecule.replace("(", "_ini")
    molecule = molecule.replace(")", "_end")
    molecule = molecule.replace("[", "_ini")
    molecule = molecule.replace("]", "_end")

    molecule_str = copy.deepcopy(molecule)
    molecule = list(molecule)

    p_counter, molecule_split = 0, []
    while not len(molecule) - 2 <= p_counter:
        if molecule[p_counter].isupper():
            if molecule[p_counter + 1].islower():
                if molecule[p_counter + 2].isnumeric():
                    numeric_return = numeric_check(pos_counter=p_counter+2, string=molecule_str)

                    molecule_split.append([molecule[p_counter] + molecule[p_counter+1], numeric_return[0]])
                    p_counter = numeric_return[1]
                else:
                    molecule_split.append([molecule[p_counter] + molecule[p_counter+1], 1])
                    p_counter += 2
            elif molecule[p_counter + 1].isnumeric():
                numeric_return = numeric_check(pos_counter=p_counter + 1, string=molecule_str)

                molecule_split.append([molecule[p_counter], numeric_return[0]])
                p_counter = numeric_return[1]
            elif molecule[p_counter + 1].isupper() or molecule[p_counter + 1] == "_":
                molecule_split.append([molecule[p_counter], 1])
                p_counter += 1

        else:
            if molecule[p_counter] == "_":
                try:
                    if molecule[p_counter + 4].isnumeric() and molecule[p_counter+1] == "e":
                        numeric_return = numeric_check(string=molecule_str, pos_counter=p_counter+4)

                        molecule_split.append([molecule[p_counter] + molecule[p_counter + 1] + molecule[p_counter + 2] +
                                               molecule[p_counter + 3], numeric_return[0]])
                        p_counter = numeric_return[1]
                    elif molecule[p_counter+1] == "e":
                        molecule_split.append([molecule[p_counter] + molecule[p_counter + 1] + molecule[p_counter + 2] +
                                               molecule[p_counter + 3], 1])
                        p_counter += 4
                    else:
                        molecule_split.append([molecule[p_counter] + molecule[p_counter + 1] + molecule[p_counter + 2] +
                                               molecule[p_counter + 3]])
                        p_counter += 4
                except IndexError:
                    molecule_split.append([molecule[p_counter] + molecule[p_counter + 1] + molecule[p_counter + 2] +
                                           molecule[p_counter + 3], 1])
                    p_counter += 4
            else:
                molecule_split.append([molecule[p_counter]])
                p_counter += 1
    else:
        if molecule[-2].isupper():
            if molecule[-1].isupper():
                molecule_split.append([molecule[-2], 1])
                molecule_split.append([molecule[-1], 1])
            elif molecule[-1].islower():
                molecule_split.append([molecule[-2] + molecule[-1], 1])
            elif molecule[-1].isnumeric():
                molecule_split.append([molecule[-2], int(molecule[-1])])
        elif molecule[-1].isupper():
            molecule_split.append([molecule[-1], 1])

    # Validity check
    bracket_val = [["_ini"], ["_end"]]
    for i in molecule_split:
        if not ((i[0] not in data.atomic_weight.keys()) or (i[0] not in bracket_val)):
            raise errors.MoleculeError("Invalid molecule")

    while ["_ini"] in molecule_split:
        p_counter = 0
        while len(molecule_split) > p_counter:
            bracket_counter, bracket_len = 0, 0
            if molecule_split[p_counter][0] == "_ini":
                bracket_start = p_counter + 1
                if molecule_split[bracket_start][0] == "_end":
                    molecule_split.pop(p_counter)
                    molecule_split.pop(bracket_start)
                    break
                else:
                    bracket_counter += 1
                    while not bracket_counter == 0:
                        if molecule_split[bracket_start + bracket_len][0] == "_ini":
                            bracket_counter += 1
                        elif molecule_split[bracket_start + bracket_len][0] == "_end":
                            bracket_counter -= 1
                        bracket_len += 1
                        if bracket_len > len(molecule_split):
                            raise errors.MoleculeError("Invalid molecule")
                    else:
                        # adjustment for error
                        bracket_len -= 1

                        multiply_value = molecule_split[bracket_len + bracket_start][1]

                        for i in range(multiply_value):
                            for k in molecule_split[bracket_start:bracket_start+bracket_len]:
                                molecule_split.append(k)

                        for i in range(0, bracket_len+2):
                            molecule_split.pop(p_counter)

                        break
            p_counter += 1

    mol_mass = 0.0
    for i in molecule_split:
        if i[0] not in data.atomic_weight.keys():
            raise errors.MoleculeError("Invalid molecule")
        mol_mass += data.atomic_weight[i[0]] * i[1]

    return mol_mass

if __name__ == "__main__":
    print()
    print("Molar mass:")
    print(round(mol_mass(str(input("Enter molecule: "))), 3))
    print()    

