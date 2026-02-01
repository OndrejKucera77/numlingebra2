"""
Převede matici v .mtx formátu ze SuiteSparse Collection do .npz formátu používaného scipy.
"""

from scipy.sparse import csr_matrix, save_npz
import matplotlib.pyplot as plt

name = "TF13"
symmetric = False   # zdali je matice symetrická
binary = False      # zdali je matice binární (obsahuje jenom 0/1)
integer = True      # zdali je matice celočíselná

M = None

with open(name + ".mtx", "r") as f:
    for line in f.readlines():
        if line[0] != "%":
            vals = line.split(" ")
            i = int(vals[0]) - 1
            j = int(vals[1]) - 1

            if M is None:
                dtype = int if binary else float
                M = csr_matrix((i+1, j+1), dtype=dtype)
            else:
                if binary:
                    M[i, j] = 1
                    if symmetric:
                        M[j, i] = 1
                elif integer:
                    M[i, j] = int(vals[2])
                    if symmetric:
                        M[j, i] = int(vals[2])
                else:
                    M[i, j] = float(vals[2])
                    if symmetric:
                        M[j, i] = float(vals[2])

save_npz(name + ".npz", M)

plt.matshow(M.todense())
plt.show()