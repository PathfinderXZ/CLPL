class MoleculeError(IndexError):
    pass

def errorCheck(arr1, arr2):
    if not len(arr1) == len(arr2):
        raise MoleculeError("Invalid molecule")