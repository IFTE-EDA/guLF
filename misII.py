import ConfigParser
import os
import re
import subprocess
import sys

mapping = {
    'inv1' : 'Inverter',
    'mux2' : '2-In_MUX',
    'or2'  : '2-In_OR',
    'or3'  : '3-In_OR',
    'or4'  : '4-In_OR',
    'and2' : '2-In_AND',
    'and3' : '3-In_AND',
    'and4' : '4-In_AND',
    'exor2': '2-In_XOR',
    'nor2' : '2-In_NOR',
    'nor3' : '3-In_NOR',
    'nor4' : '4-In_NOR',
    'nand2': '2-In_NAND',
    'nand3': '3-In_NAND',
    'nand4': '4-In_NAND'    
}

conf_dir = os.environ['APPDATA'] + '\\Logic Friday'
userlib = conf_dir + '\\user.genlib'
sizelib = conf_dir + '\\gate-sizes.ini'

try:
    f = open(sizelib)
    f.close()
except IOError:
    with open(sizelib, "w") as f:
        # save default sizes
        f.write("""\
[Gate Sizes]
Inverter = 1
2-In_NAND = 2
3-In_NAND = 3
4-In_NAND = 4
2-In_NOR = 2
3-In_NOR = 3
4-In_NOR = 4
2-In_XOR = 5.5
2-In_MUX = 4
2-In_AND = 2
3-In_AND = 2
4-In_AND = 2
2-In_OR = 2
3-In_OR = 3
4-In_OR = 4
""")

config = ConfigParser.RawConfigParser()
config.read(sizelib)

with open(userlib) as f:
    lib = f.read()

for src, dst in mapping.items():
    if config.has_option('Gate Sizes', dst):
        size = config.getfloat('Gate Sizes', dst)
        size = '%g'%size
    else:
        size = "0"
    lib = re.sub(r'( %s\t)[\d\.]+'%src, r'\g<1>%s'%size, lib)

with open(userlib, 'w') as f:
    f.write(lib)

sys.argv[0] = "misII-orig"

process = subprocess.call(sys.argv)
sys.exit(process)
