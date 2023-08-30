import sys

sys.path.append(__file__[:-22] + "data")

import copy
import errors
import re
import data


def molmass(molecule: str):
    def numeric_check(string: str, pos_counter: int):
        num = str(string[pos_counter])
        try:
            while string[pos_counter + 1].isnumeric():
                num += string[pos_counter + 1]
                pos_counter += 1
        except IndexError:
            return int(num)
        return int(num)

    errors.error_check(len(molecule), 0, 1)
    
    for i in data.Compounds.__instances__:
        if i.abbreviation == molecule:
            molecule = i.formula
    
    for group in data.FunctGroups.__instances__:
        if group.abbreviation in molecule:
            molecule = molecule.replace(group.abbreviation, group.formula)
        elif group.full_name in molecule:
            molecule = molecule.replace(group.full_name, group.formula)

    replace = {"(": "+",
               ")": "-",
               "[": "+",
               "]": "-",
               "[]": "",
               "()": "",
               " ": "",

               # isomer groups - no effect on molar mass

               "i-": "",
               "n-": "",
               "t-": "",
               "tert-": "",
               "s-": "",
               "sek-": "",
               "iso-": "",
               }
    for group, replacement in replace.items():
        molecule = molecule.replace(group, replacement)
    del replace



    errors.error_check(molecule.count("+"), molecule.count("-"), False)

    while "+" in molecule:
        p_counter = bracket_start = molecule.find("+") + 1
        bracket_counter = 1
        while not bracket_counter == 0:
            if molecule[p_counter] == "+":
                bracket_counter += 1
                p_counter += 1
            elif molecule[p_counter] == "-":
                bracket_counter += -1
                p_counter += 1
            else:
                p_counter += 1
        else:
            bracket_end = p_counter - 1
            try:
                if molecule[p_counter].isnumeric():
                    number = numeric_check(molecule, p_counter)
                    bracket_end += len(str(number))
                else:
                    number = 1
            except IndexError:
                number = 1

            molecule_part = molecule[bracket_start:bracket_end - len(str(number))]
            molecule = molecule[:bracket_start - 1] + molecule[bracket_end + 1:]
            for _ in range(number):
                molecule += molecule_part

    # valid molecule check
    checkstring = copy.copy(molecule)

    checkstring = checkstring.replace("+", "")
    checkstring = checkstring.replace("-", "")

    for element in data.Elements.__instances_re_search__:
        if element.symbol in checkstring:
            checkstring = checkstring.replace(element.symbol, "")

    if not (checkstring.isnumeric() or checkstring == ""):
        raise errors.MoleculeError
    del checkstring

    mol_mass = 0.0
    regex_digit = re.compile(r"\d+")

    for element in data.Elements.__instances_re_search__:
        regex_n = re.compile(element.symbol + r"\d+")
        regex = re.compile(element.symbol)

        w_numbers = re.findall(regex_n, molecule)
        no_numbers = re.findall(regex, molecule)

        for k in w_numbers:
            number = int(re.findall(regex_digit, k)[0])
            mol_mass += number * element.atomic_weight
        mol_mass += (len(no_numbers) - len(w_numbers)) * element.atomic_weight

    return mol_mass


if __name__ == "__main__":
    print(round(molmass(str(input("Enter molecule: "))), 3))
    print()
