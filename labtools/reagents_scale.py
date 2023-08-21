def reagent_scale():
    init_eq = int(input("Equivalents of the constant reagent: "))
    init_mass = float(input("Mass of the constant reagent: "))
    init_molar_mass = float(input("Molar mass of the constant reagent: "))
    print()
    init_amount = init_mass/(init_molar_mass * init_eq)
    for i in range(0, int(input("Reagents to scale: "))):
        molar_mass = float(input(f"Molar mass of reagent {i}: "))
        eq = int(input(f"Eq of reagent {i}: "))
        print()
        print(f"Mass of reagent {i} is {init_amount*eq*molar_mass}")
        print()

if __name__ == "__main__":
	reagent_scale()

