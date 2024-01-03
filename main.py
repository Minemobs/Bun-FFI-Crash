import itertools
from string import ascii_lowercase as alphabet

def all_strings():
    numbers = map(str, range(1, 11))
    return map(''.join, itertools.product(alphabet, alphabet, numbers, alphabet, alphabet))

functionNames = list(itertools.islice(all_strings(), 700))

with open('functions.c', 'w+') as writer:
    writer.write("\n".join(map(lambda s: f"void {s}(){{}}", functionNames)))
    
with open('functions.h', 'w+') as writer:
    writer.write("\n".join(map(lambda s: f"void {s}();", functionNames)))

with open('ffi.ts', "w+") as writer:
    writer.write("import { dlopen, suffix } from 'bun:ffi';\n\nexport const functionsFFI = dlopen(`functions.${suffix}`, {\n")
    writer.write("\n".join(map(lambda s: f"{s}: {{}},", functionNames)))
    writer.write("\n});\n")
