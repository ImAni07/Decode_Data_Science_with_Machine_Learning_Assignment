"""
    Question No. - 11:
    Define a Python module named constants.py containing constants like pi and the speed of light.
"""

# This script consist of a module named constants
# Constants module

PI = 3.141592653589793
SPEED_OF_LIGHT = 299792458  # in meters per second
GRAVITATIONAL_CONSTANT = 6.67430e-11  # in m^3 kg^-1 s^-2
PLANCK_CONSTANT = 6.62607015e-34  # in m^2 kg / s

# Printing the Constants

import constants

print("PI: ", constants.PI)
print("SPEED_OF_LIGHT: ", constants.SPEED_OF_LIGHT)
print("GRAVITATIONAL_CONSTANT: ", constants.GRAVITATIONAL_CONSTANT)
print("PLANCK_CONSTANT: ", constants.PLANCK_CONSTANT)

# Output:
"""
    PI:  3.141592653589793
    SPEED_OF_LIGHT:  299792458
    GRAVITATIONAL_CONSTANT:  6.6743e-11
    PLANCK_CONSTANT:  6.62607015e-34
"""

# Step-by-Step Process
"""
    Step 1: Create a new file and name it {constant.py}
    Step 2: In the file {constants.py}, define constants like 'PI' and 'SPEED_OF_LIGHT', with their respective values
    Step 3: Save the file.
"""