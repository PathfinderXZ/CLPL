import os
from dotenv import load_dotenv
from datadef import FunctGroups

load_dotenv(__file__[:-14] + "config/.env")

if os.getenv("ORGANIC_CHEMISTRY_MODE_ON"):
    Methyl = FunctGroups(
        abbreviation="Me",
        full_name="Methyl",
        formula="(CH3)",
    )

    Ethyl = FunctGroups(
        abbreviation="Et",
        full_name="Ethyl",
        formula="(CH3CH2)",
    )

    Propyl = FunctGroups(
        abbreviation="Pr",
        full_name="Propyl",
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
        full_name="Pentyl",
        formula="(CH3(CH2)4)",
    )

    Cyclohexyl = FunctGroups(
        abbreviation="CyHex",
        full_name="Cyclohexyl",
        formula="(CH(CH2)5)",
    )

    Hexyl = FunctGroups(
        abbreviation="Hex",
        full_name="Hexyl",
        formula="(CH3(CH2)5)",
    )

    Phenyl = FunctGroups(
        abbreviation="Ph",
        full_name="Phenyl",
        formula="(C6H5)",
    )

    Benzyl = FunctGroups(
        abbreviation="Bz",
        full_name="Benzyl",
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
