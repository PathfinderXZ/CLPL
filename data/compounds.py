import os
from dotenv import load_dotenv
from datadef import Compounds


load_dotenv(__file__[:-17] + "config/.env")

if os.getenv("ORGANIC_CHEMISTRY_MODE_ON"):
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
