def theoretical_yield():
    molar_mass = []
    mass = []
    eq = []
    print("All units in grams or g/mol")
    for i in range(1, int(input("Number of reactants: "))+1):
        mass.append(float(input("Weight of reactant " + str(i) + " used: ")))
        molar_mass.append(float(input("Molar mass of reactant " + str(i) + ": ")))
        eq.append(int(input("Equivalents of reactant " + str(i) + " in reaction: ")))
        print()

    equivalent_molar_amount = []
    for i in range(0, len(mass)-1):
        equivalent_molar_amount.append((mass[i]/molar_mass[i])/eq[i])
    product_molar_mass = float(input("Molar mass of product: "))
    product_eq = int(input("Equivalents of product in reaction: "))

    theoretical = str(min(equivalent_molar_amount)*product_eq*product_molar_mass)
    print()
    print(f"Theoretical yield: {theoretical} g")
    print()
    return float(theoretical)


def percent_yield():
    theoretical = theoretical_yield()
    print()
    actual = float(input("Practical yield of product [g]: "))

    percent = (actual / theoretical) * 100
    print()
    print(f"Percent yield is {str(percent)} %")
    print()
    return percent

if __name__ == "__main__":
    percent_yield()
