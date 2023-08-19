import unittest
import random

import data

import molmass
from labtools import molar_mass


def generate_formula():
    return_str = ""
    for i in range(random.randint(2, 2)):
        element = list(data.atomic_weight.keys())[random.randint(0, 108)]
        count = str(random.randint(1, 1))
        if count == "1":
            count = ""
        return_str += element + count
    return return_str


class TestSum(unittest.TestCase):
    def test_mass1(self):
        for _ in range(1, 500000):
            form = generate_formula()

            res1 = round(molmass.Formula(form).mass, 3)
            res2 = round(molar_mass.molar_mass(form), 3)

            self.assertEqual(res1, res2)


if __name__ == "__main__":
    unittest.main()
