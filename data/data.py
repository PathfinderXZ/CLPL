import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv(__file__[:-12] + "config")


@dataclass
class Elements:
    symbol: str
    atomic_number: int
    atomic_weight: float
    electron_configuration: str
    column: int
    row: int
    stable: bool

    __instances__ = []
    __instances_re_search__ = []

    def __init__(self, symbol: str, atomic_number: int, atomic_mass: float, column: int, row: int,
                 stable=True, alternate_name=None, stable_oxidation_states=None, natural_oxidation_states=None,
                 most_stable_isotope_time_of_decay=None):
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.atomic_weight = atomic_mass
        self.electron_configuration = ""
        self.column = column
        self.row = row
        self.alternative_name = alternate_name
        self.stable = stable
        self.stable_oxidation_states = stable_oxidation_states
        self.naturally_occurring_oxidation_states = natural_oxidation_states

        if not stable:
            self.most_stable_isotope_time_of_decay = most_stable_isotope_time_of_decay

        Elements.__instances__.append(self)
        Elements.__instances_re_search__.append(self)


    @staticmethod
    def sort_instances():
        n = len(Elements.__instances__)
        swapped = False
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if Elements.__instances__[j].atomic_number > Elements.__instances__[j + 1].atomic_number:
                    swapped = True
                    Elements.__instances__[j], Elements.__instances__[j + 1] = (Elements.__instances__[j + 1],
                                                                                Elements.__instances__[j])
            if not swapped:
                return

    def create_electron_config(self):
        pass


Helium = Elements(
    symbol="He",
    atomic_number=2,
    atomic_mass=4.002602,
    column=18,
    row=1
    )

Lithium = Elements(
    symbol="Li",
    atomic_number=3,
    atomic_mass=6.941,
    column=1,
    row=2
    )

Beryllium = Elements(
    symbol="Be",
    atomic_number=4,
    atomic_mass=9.0121831,
    column=2,
    row=2
    )

Neon = Elements(
    symbol="Ne",
    atomic_number=10,
    atomic_mass=20.1797,
    column=18,
    row=2
    )

Sodium = Elements(
    symbol="Na",
    atomic_number=11,
    atomic_mass=22.98976928,
    column=1,
    row=3,
    )

Magnesium = Elements(
    symbol="Mg",
    atomic_number=12,
    atomic_mass=24.3051,
    column=2,
    row=3,
    )

Aluminium = Elements(
    symbol="Al",
    atomic_number=13,
    atomic_mass=26.9815385,
    column=13,
    row=3,
    alternate_name="Aluminum"
    )

Silicon = Elements(
    symbol="Si",
    atomic_number=14,
    atomic_mass=28.0855,
    column=14,
    row=3,
    )

Chlorine = Elements(
    symbol="Cl",
    atomic_number=17,
    atomic_mass=35.4529,
    column=17,
    row=3,
    )

Argon = Elements(
    symbol="Ar",
    atomic_number=18,
    atomic_mass=39.948,
    column=18,
    row=3,
    )

Calcium = Elements(
    symbol="Ca",
    atomic_number=20,
    atomic_mass=40.078,
    column=2,
    row=4,
    )

Scandium = Elements(
    symbol="Sc",
    atomic_number=21,
    atomic_mass=44.955908,
    column=3,
    row=4,
    )

Titanium = Elements(
    symbol="Ti",
   atomic_number=22,
   atomic_mass=47.867,
   column=4,
   row=4,
   )

Chromium = Elements(
    symbol="Cr",
    atomic_number=24,
    atomic_mass=51.9961,
    column=6,
    row=4,
    )

Manganese = Elements(
    symbol="Mn",
    atomic_number=25,
    atomic_mass=54.938044,
    column=7,
    row=4,
    )

Iron = Elements(
    symbol="Fe",
    atomic_number=26,
    atomic_mass=55.845,
    column=8,
    row=4,
    )

Cobalt = Elements(
    symbol="Co",
    atomic_number=27,
    atomic_mass=58.933194,
    column=9,
    row=4,
    )

Nickel = Elements(
    symbol="Ni",
    atomic_number=28,
    atomic_mass=58.6934,
    column=10,
    row=4,
    )

Copper = Elements(
    symbol="Cu",
    atomic_number=29,
    atomic_mass=63.546,
    column=11,
    row=4,
    )

Zinc = Elements(
    symbol="Zn",
    atomic_number=30,
    atomic_mass=65.38,
    column=12,
    row=4,
    )

Gallium = Elements(
    symbol="Ga",
    atomic_number=31,
    atomic_mass=69.723,
    column=13,
    row=4,
    )

Germanium = Elements(
    symbol="Ge",
    atomic_number=32,
    atomic_mass=72.63,
    column=14,
    row=4,
    )

Arsenic = Elements(
    symbol="As",
    atomic_number=33,
    atomic_mass=74.921595,
    column=15,
    row=4,
    )

Selenium = Elements(
    symbol="Se",
    atomic_number=34,
    atomic_mass=78.971,
    column=16,
    row=4,
    )

Bromine = Elements(
    symbol="Br",
    atomic_number=35,
    atomic_mass=79.9035,
    column=17,
    row=4,
    )

Krypton = Elements(
    symbol="Kr",
    atomic_number=36,
    atomic_mass=83.798,
    column=18,
    row=4,
    )

Rubidium = Elements(
    symbol="Rb",
    atomic_number=37,
    atomic_mass=85.4678,
    column=1,
    row=5,
    )

Strontium = Elements(
    symbol="Sr",
    atomic_number=38,
    atomic_mass=87.62,
    column=2,
    row=5,
    )

Zirconium = Elements(
    symbol="Zr",
    atomic_number=40,
    atomic_mass=91.224,
    column=4,
    row=5,
    )

Niobium = Elements(
    symbol="Nb",
    atomic_number=41,
    atomic_mass=92.90637,
    column=5,
    row=5,
    )

Molybdenum = Elements(
    symbol="Mo",
    atomic_number=42,
    atomic_mass=95.95,
    column=6,
    row=5,
    )

Technetium = Elements(
    symbol="Tc",
    atomic_number=43,
    atomic_mass=97.9072,
    column=7,
    row=5,
    )

Ruthenium = Elements(
    symbol="Ru",
    atomic_number=44,
    atomic_mass=101.07,
    column=8,
    row=5,
    )

Rhodium = Elements(
    symbol="Rh",
    atomic_number=45,
    atomic_mass=102.9055,
    column=9,
    row=5,
    )

Palladium = Elements(
    symbol="Pd",
    atomic_number=46,
    atomic_mass=106.42,
    column=10,
    row=5,
    )

Silver = Elements(
    symbol="Ag",
    atomic_number=47,
    atomic_mass=107.8682,
    column=11,
    row=5,
    )

Cadmium = Elements(symbol="Cd",
                   atomic_number=48,
                   atomic_mass=112.414,
                   column=12,
                   row=5,
                   )

Indium = Elements(symbol="In",
                  atomic_number=49,
                  atomic_mass=114.818,
                  column=13,
                  row=5,
                  )

Tin = Elements(symbol="Sn",
               atomic_number=50,
               atomic_mass=118.71,
               column=14,
               row=5,
               )

Antimony = Elements(symbol="Sb",
                    atomic_number=51,
                    atomic_mass=121.76,
                    column=15,
                    row=5,
                    )

Tellurium = Elements(symbol="Te",
                     atomic_number=52,
                     atomic_mass=127.6,
                     column=16,
                     row=5,
                     )

Xenon = Elements(symbol="Xe",
                 atomic_number=54,
                 atomic_mass=131.293,
                 column=18,
                 row=5,
                 )

Caesium = Elements(symbol="Cs",
                   atomic_number=55,
                   atomic_mass=132.90545196,
                   column=1,
                   row=6,
                   )

Barium = Elements(symbol="Ba",
                  atomic_number=56,
                  atomic_mass=137.327,
                  column=2,
                  row=6,
                  )

Lanthanum = Elements(symbol="La",
                     atomic_number=57,
                     atomic_mass=138.90547,
                     column=3,
                     row=6,
                     )

Cerium = Elements(symbol="Ce",
                  atomic_number=58,
                  atomic_mass=140.116,
                  column=0,
                  row=6,
                  )

Praseodymium = Elements(symbol="Pr",
                        atomic_number=59,
                        atomic_mass=140.90766,
                        column=0,
                        row=6,
                        )

Neodymium = Elements(symbol="Nd",
                     atomic_number=60,
                     atomic_mass=144.242,
                     column=0,
                     row=6,
                     )

Promethium = Elements(symbol="Pm",
                      atomic_number=61,
                      atomic_mass=144.9128,
                      column=0,
                      row=6,
                      )

Samarium = Elements(symbol="Sm",
                    atomic_number=62,
                    atomic_mass=150.36,
                    column=0,
                    row=6,
                    )

Europium = Elements(symbol="Eu",
                    atomic_number=63,
                    atomic_mass=151.964,
                    column=0,
                    row=6,
                    )

Gadolinium = Elements(symbol="Gd",
                      atomic_number=64,
                      atomic_mass=157.25,
                      column=0,
                      row=6,
                      )

Terbium = Elements(symbol="Tb",
                   atomic_number=65,
                   atomic_mass=158.92535,
                   column=0,
                   row=6,
                   )

Dysprosium = Elements(symbol="Dy",
                      atomic_number=66,
                      atomic_mass=162.5,
                      column=0,
                      row=6,
                      )

Holmium = Elements(symbol="Ho",
                   atomic_number=67,
                   atomic_mass=164.93033,
                   column=0,
                   row=6,
                   )

Erbium = Elements(symbol="Er",
                  atomic_number=68,
                  atomic_mass=167.259,
                  column=0,
                  row=6,
                  )

Thulium = Elements(symbol="Tm",
                   atomic_number=69,
                   atomic_mass=168.93422,
                   column=0,
                   row=6,
                   )

Ytterbium = Elements(symbol="Yb",
                     atomic_number=70,
                     atomic_mass=173.054,
                     column=0,
                     row=6,
                     )

Lutetium = Elements(symbol="Lu",
                    atomic_number=71,
                    atomic_mass=174.9668,
                    column=0,
                    row=6,
                    )

Hafnium = Elements(symbol="Hf",
                   atomic_number=72,
                   atomic_mass=178.49,
                   column=4,
                   row=6,
                   )

Tantalum = Elements(symbol="Ta",
                    atomic_number=73,
                    atomic_mass=180.94788,
                    column=5,
                    row=6,
                    )

Tungsten = Elements(symbol="W",
                    atomic_number=74,
                    atomic_mass=183.84,
                    column=6,
                    row=6,
                    )

Rhenium = Elements(symbol="Re",
                   atomic_number=75,
                   atomic_mass=186.207,
                   column=7,
                   row=6,
                   )

Osmium = Elements(symbol="Os",
                  atomic_number=76,
                  atomic_mass=190.23,
                  column=8,
                  row=6,
                  )

Iridium = Elements(symbol="Ir",
                   atomic_number=77,
                   atomic_mass=192.217,
                   column=9,
                   row=6,
                   )

Platinum = Elements(symbol="Pt",
                    atomic_number=78,
                    atomic_mass=195.084,
                    column=10,
                    row=6,
                    )

Gold = Elements(symbol="Au",
                atomic_number=79,
                atomic_mass=196.966569,
                column=11,
                row=6,
                )

Mercury = Elements(symbol="Hg",
                   atomic_number=80,
                   atomic_mass=200.592,
                   column=12,
                   row=6,
                   )

Thallium = Elements(symbol="Tl",
                    atomic_number=81,
                    atomic_mass=204.3834,
                    column=13,
                    row=6,
                    )

Lead = Elements(symbol="Pb",
                atomic_number=82,
                atomic_mass=207.2,
                column=14,
                row=6,
                )

Bismuth = Elements(symbol="Bi",
                   atomic_number=83,
                   atomic_mass=208.9804,
                   column=15,
                   row=6,
                   stable=False,
                   )

Polonium = Elements(symbol="Po",
                    atomic_number=84,
                    atomic_mass=208.9824,
                    column=16,
                    row=6,
                    )

Astatine = Elements(symbol="At",
                    atomic_number=85,
                    atomic_mass=209.9871,
                    column=17,
                    row=6,
                    stable=False,
                    )

Radon = Elements(symbol="Rn",
                 atomic_number=86,
                 atomic_mass=222.0176,
                 column=18,
                 row=6,
                 stable=False,
                 )

Francium = Elements(symbol="Fr",
                    atomic_number=87,
                    atomic_mass=223.0197,
                    column=1,
                    row=7,
                    stable=False,
                    )

Radium = Elements(symbol="Ra",
                  atomic_number=88,
                  atomic_mass=226.0254,
                  column=2,
                  row=7,
                  stable=False,
                  )

Actinium = Elements(symbol="Ac",
                    atomic_number=89,
                    atomic_mass=227.0278,
                    column=3,
                    row=7,
                    stable=False,
                    )

Thorium = Elements(symbol="Th",
                   atomic_number=90,
                   atomic_mass=232.0377,
                   column=0,
                   row=7,
                   stable=False,
                   )

Protactinium = Elements(symbol="Pa",
                        atomic_number=91,
                        atomic_mass=231.03588,
                        column=0,
                        row=7,
                        stable=False,
                        )

Uranium = Elements(symbol="U",
                   atomic_number=92,
                   atomic_mass=238.02891,
                   column=0,
                   row=7,
                   stable=False,
                   )

Neptunium = Elements(symbol="Np",
                     atomic_number=93,
                     atomic_mass=237.0482,
                     column=0,
                     row=7,
                     stable=False,
                     )

Plutonium = Elements(symbol="Pu",
                     atomic_number=94,
                     atomic_mass=244.0642,
                     column=0,
                     row=7,
                     stable=False,
                     )

Americium = Elements(symbol="Am",
                     atomic_number=95,
                     atomic_mass=243.0614,
                     column=0,
                     row=7,
                     stable=False,
                     )

Curium = Elements(symbol="Cm",
                  atomic_number=96,
                  atomic_mass=247.0704,
                  column=0,
                  row=7,
                  stable=False,
                  )

Berkelium = Elements(symbol="Bk",
                     atomic_number=97,
                     atomic_mass=247.0703,
                     column=0,
                     row=7,
                     stable=False,
                     )

Californium = Elements(symbol="Cf",
                       atomic_number=98,
                       atomic_mass=251.0796,
                       column=0,
                       row=7,
                       stable=False,
                       )

Einsteinium = Elements(symbol="Es",
                       atomic_number=99,
                       atomic_mass=252.083,
                       column=0,
                       row=7,
                       stable=False,
                       )

Fermium = Elements(symbol="Fm",
                   atomic_number=100,
                   atomic_mass=257.0951,
                   column=0,
                   row=7,
                   stable=False,
                   )

Mendelevium = Elements(symbol="Md",
                       atomic_number=101,
                       atomic_mass=258.0984,
                       column=0,
                       row=7,
                       stable=False,
                       )

Nobelium = Elements(
    symbol="No",
    atomic_number=102,
    atomic_mass=259.101,
    column=0,
    row=7,
    stable=False,
)

Lawrencium = Elements(
    symbol="Lr",
    atomic_number=103,
    atomic_mass=262.1096,
    column=0,
    row=7,
    stable=False,
)

Rutherfordium = Elements(
    symbol="Rf",
    atomic_number=104,
    atomic_mass=267.1218,
    column=4,
    row=8,
    stable=False,
)

Dubnium = Elements(
    symbol="Db",
    atomic_number=105,
    atomic_mass=268.1257,
    column=5,
    row=8,
    stable=False,
)

Seaborgium = Elements(
    symbol="Sg",
    atomic_number=106,
    atomic_mass=271.1339,
    column=6,
    row=8,
)

Bohrium = Elements(
    symbol="Bh",
    atomic_number=107,
    atomic_mass=272.1383,
    column=7,
    row=8,
    stable=False,
)

Hassium = Elements(
    symbol="Hs",
    atomic_number=108,
    atomic_mass=270.1343,
    column=8,
    row=8,
    stable=False,
)

Meitnerium = Elements(
    symbol="Mt",
    atomic_number=109,
    atomic_mass=276.1516,
    column=9,
    row=8,
    stable=False,
)

#
#
#

Hydrogen = Elements(
    symbol="H",
    atomic_number=1,
    atomic_mass=1.007941,
    column=1,
    row=1
)

Boron = Elements(
    symbol="B",
    atomic_number=5,
    atomic_mass=10.811,
    column=13,
    row=2
)

Carbon = Elements(
    symbol="C",
    atomic_number=6,
    atomic_mass=12.01074,
    column=14,
    row=2
)

Nitrogen = Elements(
    symbol="N",
    atomic_number=7,
    atomic_mass=14.006703,
    column=15,
    row=2
)

Oxygen = Elements(
    symbol="O",
    atomic_number=8,
    atomic_mass=15.999405,
    column=16,
    row=2
)

Fluorine = Elements(
    symbol="F",
    atomic_number=9,
    atomic_mass=18.998403163,
    column=17,
    row=2
)

Phosphorus = Elements(
    symbol="P",
    atomic_number=15,
    atomic_mass=30.973761998,
    column=15,
    row=3,
)

Sulfur = Elements(
    symbol="S",
    atomic_number=16,
    atomic_mass=32.0648,
    column=16,
    row=3,
)

Potassium = Elements(
    symbol="K",
    atomic_number=19,
    atomic_mass=39.0983,
    column=1,
    row=4,
)

Vanadium = Elements(
    symbol="V",
    atomic_number=23,
    atomic_mass=50.9415,
    column=5,
    row=4,
)


Yttrium = Elements(
    symbol="Y",
    atomic_number=39,
    atomic_mass=88.90584,
    column=3,
    row=5,
)

Iodine = Elements(
    symbol="I",
    atomic_number=53,
    atomic_mass=126.90447,
    column=17,
    row=5,
)

#

Deuterium = Elements(
    symbol="D",
    atomic_number=Hydrogen.atomic_number,
    atomic_mass= 2.014,
    column=Hydrogen.column,
    row=Hydrogen.row
)

@dataclass
class Isotopes(Elements):
    pass


@dataclass
class Compounds:
    full_name: str
    abbreviation: str
    formula: str

    __instances__ = []

    def __init__(self, formula: str, abbreviation: str, full_name: str):
        self.abbreviation = abbreviation
        self.formula = formula
        self.full_name = full_name

        Compounds.__instances__.append(self)


@dataclass
class FunctGroups:
    full_name: str
    abbreviation: str
    formula: str

    __instances__ = []

    def __init__(self, abbreviation: str, full_name: str, formula: str):
        self.abbreviation = abbreviation
        self.full_name = full_name
        self.formula = formula

        FunctGroups.__instances__.append(self)


monohydrate = FunctGroups(
    abbreviation=None,
    full_name="monohydrate",
    formula="(H2O)"
)

dihydrate = FunctGroups(
    abbreviation=None,
    full_name="dihydrate",
    formula="((H2O)2)"
)

trihydrate = FunctGroups(
    abbreviation=None,
    full_name="trihydrate",
    formula="((H2O)3)"
)

tetrahydrate = FunctGroups(
    abbreviation=None,
    full_name="tetrahydrate",
    formula="((H2O)4)"
)

pentahydrate = FunctGroups(
    abbreviation=None,
    full_name="pentahydrate",
    formula="((H2O)5)"
)

hexahydrate = FunctGroups(
    abbreviation=None,
    full_name="hexahydrate",
    formula="((H2O)6)"
)

heptahydrate = FunctGroups(
    abbreviation=None,
    full_name="heptahydrate",
    formula="((H2O)7)"
)

octahydrate = FunctGroups(
    abbreviation=None,
    full_name="octahydrate",
    formula="((H2O)8)"
)

nonahydrate = FunctGroups(
    abbreviation=None,
    full_name="nonahydrate",
    formula="((H2O)9)"
)

decahydrate = FunctGroups(
    abbreviation=None,
    full_name="decahydrate",
    formula="((H2O)10)"
)

undecahydrate = FunctGroups(
    abbreviation=None,
    full_name="undecahydrate",
    formula="((H2O)11)"
)

dodecahydrate = FunctGroups(
    abbreviation=None,
    full_name="dodecahydrate",
    formula="((H2O)12)"
)

if os.getenv("ORGANIC_CHEMISTRY_MODE_ON"):
    # groups

    # Compounds
    DMSO = Compounds(
        abbreviation="DMSO",
        full_name="Dimethyl sulfoxide",
        formula="(C2H6OS)",
    )

    THF = Compounds(
        abbreviation= "THF",
        full_name="Tetrahydrofurane",
        formula= "(C4H8O)",
    )

    DMAC = Compounds(
        abbreviation="DMAC",
        full_name="Dimethylacetamide",
        formula= "(C4H9NO)",
    )

    DMF = Compounds(
        abbreviation="DMF",
        full_name="Dimethylformamide",
        formula="(C3H7NO)",
    )

    DCM = Compounds(
        abbreviation="DCM",
        full_name="Dichloromethane",
        formula="(CH2Cl2)"
    )

    NHS = Compounds(
        abbreviation="NHS",
        full_name="N-Hydroxysuccinimide",
        formula="((CH2CO)2NOH)",
    )

    AcN = Compounds(
        abbreviation="AcN",
        full_name="Acetonitrile",
        formula="(MeCN)",
    )

    DMAP = Compounds(
        abbreviation="DMAP",
        full_name="4-Dimethylaminopyridine",
        formula="((CH3)2NC5H4N)",
    )

    DEAD = Compounds(
        abbreviation="DEAD",
        full_name="Diethyl azodicarboxylate",
        formula="(NCO2CH2CH3)2)",

    )

    DEADCAT = Compounds(
        abbreviation="DEADCAT",
        full_name=DEAD.full_name,
        formula=DEAD.formula,
    )

    LDA = Compounds(
        abbreviation="LDA",
        full_name="Lithium diisopropylamide",
        formula="(LiN(CH(CH3)2)2)",
    )

    Py = Compounds(
        abbreviation="Py",
        full_name = "Pyridine",
        formula="(C5H5N)",
    )

    LAH = Compounds(
        abbreviation="LAH",
        full_name="Lithium aluminium hydride",
        formula="(LiAlH4)",
    )

    # groups

    Methyl = FunctGroups(
        abbreviation="Me",
        full_name = "Methyl",
        formula="(CH3)",
    )

    Ethyl = FunctGroups(
        abbreviation="Et",
        full_name = "Ethyl",
        formula="(CH3CH2)",
    )

    Propyl = FunctGroups(
        abbreviation="Pr",
        full_name = "Propyl",
        formula="(CH3(CH2)2)",
    )

    Butyl = FunctGroups(
        abbreviation="Bu",
        full_name="Butyl",
        formula="(CH3(CH2)3",
    )

    Butyl_2 = FunctGroups(
        abbreviation="But",
        full_name=Butyl.full_name,
        formula=Butyl.formula
    )
    
    Pentyl = FunctGroups(
        abbreviation="Pent",
        full_name = "Pentyl",
        formula="(CH3(CH2)4)",
    )

    Cyclohexyl = FunctGroups(
        abbreviation="CyHex",
        full_name="Cyclohexyl",
        formula="(CH(CH2)5)",
    )

    Hexyl = FunctGroups(
        abbreviation="Hex",
        full_name = "Hexyl",
        formula="(CH3(CH2)5)",
    )

    Phenyl = FunctGroups(
        abbreviation="Ph",
        full_name = "Phenyl",
        formula="(C6H5)",
    )

    Benzyl = FunctGroups(
        abbreviation="Bz",
        full_name = "Benzyl",
        formula="(C6H5CH2)",
    )

    Tosyl = FunctGroups(
        abbreviation="Ts",
        full_name="Tosyl",
        formula="(SO2C6H4CH3)",
    )

    Acetoacetonate = FunctGroups(
        abbreviation="acac",
        full_name="Acetylacetonate(-1) ligand",
        formula="(C5H7O2)",
    )

    Acetyl = FunctGroups(
        abbreviation="Ac",
        full_name="Acetyl",
        formula="CH3CO",
    )

Elements.sort_instances() 
