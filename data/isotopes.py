from datadef import Isotopes
from elements import *

deuterium = Isotopes(
    element=Hydrogen,
    full_name="Deuterium",
    symbol="D",
    neutron_number=1,
    atomic_weight=2.0141,
    stable=True,
    half_life=["stable", None]
)

tritium = Isotopes(
    element=Hydrogen,
    full_name="Tritium",
    symbol="H-3",
    neutron_number=2,
    atomic_weight=3.016049,
    stable=False,
    half_life=[12.33, "years"]
)