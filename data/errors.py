class MoleculeError(TypeError):
    pass

class AttributeError(ValueError):
    pass

def error_check(n1, n2, truefalse):
    if n1 == n2 and truefalse:
        raise MoleculeError("Invalid molecule")
    elif not truefalse and not n1 == n2:
        raise MoleculeError("Invalid molecule")

