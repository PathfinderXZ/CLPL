from dataclasses import dataclass
from registry import _Registry


@dataclass
class Elements(_Registry):
    symbol: str
    full_name: str
    atomic_number: int
    atomic_weight: float
    short_electron_config: str
    full_electron_config: str
    column: int
    row: int
    stable: bool
    stable_oxidation_states: str
    naturally_occurring_oxidation_states: str
    most_stable_isotope_half_life: list

    _registry = []
    _re_registry = []

    def __init__(self, symbol: str, atomic_number: int, atomic_mass: float, column: int, row: int,  full_name="",
                 stable=True, alternate_name=[], full_electron_config="", short_electron_config="",
                 stable_oxidation_states=[], natural_oxidation_states=[], most_stable_isotope_half_life=["stable", None]):

        self.alternative_name = alternate_name
        self.full_name = full_name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.atomic_weight = atomic_mass

        self.full_electron_config = full_electron_config
        self.short_electron_config = short_electron_config

        self.column = column
        self.row = row

        self.stable = stable
        self.most_stable_isotope_half_life = most_stable_isotope_half_life

        self.stable_oxidation_states = stable_oxidation_states
        self.naturally_occurring_oxidation_states = natural_oxidation_states
        self.most_stable_isotope_half_life = most_stable_isotope_half_life

        Elements._registry.append(self)

    @staticmethod
    def _sort_instances_re():
        len_one = []
        for element in Elements._registry:
            if len(element.symbol) == 1:
                len_one.append(element)
            else:
                Elements._re_registry.append(element)

        for element in len_one:
            Elements._re_registry.append(element)

        del len_one



    def create_electron_config(self):
        fill_order = ("1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p",
                        "7s", "5f", "6d", "7p",)
        electron_capacity = {
            "s": 2,
            "p": 6,
            "d": 10,
            "f": 14,
        }

        if self.full_electron_config == "":
            electrons_filled = 0
            for orbital in fill_order:
                if self.atomic_number - electrons_filled >= electron_capacity[orbital[1]]:
                    self.full_electron_config += f"{orbital}{electron_capacity[orbital[1]]} "
                    electrons_filled += electron_capacity[orbital[1]]

                elif (self.atomic_number - electrons_filled < electron_capacity[orbital[1]] and
                      not self.atomic_number - electrons_filled == 0):
                    self.full_electron_config += f"{orbital}{self.atomic_number - electrons_filled}"
                    break
                elif self.atomic_number - electrons_filled == 0:
                    break

        if self.short_electron_config == "":
            noble_gasses = (("He", 2, "1s2"),
                            ("Ne", 10, "1s2 2s2 2p6"),
                            ("Ar", 18, "1s2 2s2 2p6 3s2 3p6"),
                            ("Kr", 36, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6"),
                            ("Xe", 54, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6"),
                            ("Rn", 86, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6"),
                            ("Og", 118, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p6"))

            last_ng = noble_gasses[0]
            for ng in noble_gasses:
                if self.atomic_number > ng[1]:
                    last_ng = ng
                else:
                    self.short_electron_config = self.full_electron_config.replace(last_ng[2], f"[{last_ng[0]}]")
                    break

    @staticmethod
    def _class_create_electron_config():
        for element in Elements._registry:
            element.create_electron_config()


@dataclass
class Isotopes(_Registry):
    element: Elements
    full_name: str
    symbol: str
    atomic_number: int
    neutron_number: int
    atomic_weight: float
    stable: bool
    half_life: []


    _registry = []

    def __init__(self, element, full_name, neutron_number, atomic_weight, symbol="", stable=True, half_life=[]):
        self.Element = element
        self.atomic_number = element.atomic_number
        self.full_name = full_name
        self.symbol = symbol
        self.neutron_number = neutron_number
        self.atomic_weight = atomic_weight
        self.stable = stable
        self.half_life = half_life

        Isotopes._registry.append(self)



@dataclass
class Compounds(_Registry):
    full_name: str
    abbreviation: str
    formula: str

    _registry = []

    def __init__(self, formula: str, abbreviation: str, full_name: str):
        self.abbreviation = abbreviation
        self.formula = formula
        self.full_name = full_name

        Compounds._registry.append(self)


@dataclass
class FunctGroups(_Registry):
    full_name: str
    abbreviation: str
    formula: str

    _registry = []

    def __init__(self, abbreviation: str, full_name: str, formula: str):
        self.abbreviation = abbreviation
        self.full_name = full_name
        self.formula = formula

        if not self.formula:
            raise ValueError

        if not self.abbreviation and not self.formula:
            self.abbreviation = self.formula
            self.full_name = self.formula
        elif not self.abbreviation:
            self.abbreviation = self.full_name
        elif not self.full_name:
            self.full_name = self.abbreviation

        FunctGroups._registry.append(self)
