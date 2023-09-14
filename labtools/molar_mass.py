import sys

sys.path.append(__file__[:-22] + "data")

import copy
import errors
import re

import datadef
import compounds
import elements
import groups
import isotopes


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
    
    for compound in datadef.Compounds.registry():
        if compound.abbreviation == molecule:
            molecule = molecule.replace(compound.abbreviation, compound.formula)

    for group in datadef.FunctGroups.registry():
        if group.full_name in molecule:
            molecule = molecule.replace(group.full_name, group.formula)

    for group in datadef.FunctGroups.registry():
        if group.abbreviation in molecule:
            molecule = molecule.replace(group.abbreviation, group.formula)


    replace = {"(": "+",
               ")": "_",
               "[": "+",
               "]": "_",
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



    errors.error_check(molecule.count("+"), molecule.count("_"), False)

    while "+" in molecule:
        p_counter = bracket_start = molecule.find("+") + 1
        bracket_counter = 1
        while not bracket_counter == 0:
            if molecule[p_counter] == "+":
                bracket_counter += 1
                p_counter += 1
            elif molecule[p_counter] == "_":
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
    checkstring = checkstring.replace("_", "")

    for element in datadef.Elements.re_lookup_registry():
        if element.symbol in checkstring:
            checkstring = checkstring.replace(element.symbol, "")

    if not (checkstring.isnumeric() or checkstring == ""):
        raise errors.MoleculeError
    del checkstring

    mol_mass = 0.0
    regex_digit = re.compile(r"\d+")

    #preemptive isotope search

    # for isotope in datadef.Isotopes.registry():
    #     if len(isotope.symbol) > 1:
    #         regex_n = re.compile(isotope.symbol + r"\d+")
    #         regex = re.compile(isotope.symbol)
    #
    #         w_numbers = re.findall(regex_n, molecule)
    #         no_numbers = re.findall(regex, molecule)


    for element in datadef.Elements.re_lookup_registry():
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
