def pdb2lmp():
    pdb = open("2qna.pdb",'r')
    out = open("kapB_lmp_mol.data","w")
    type = []
    index = []
    x = []
    y = []
    z = []

    for line in pdb:
        word = line.split()
        if word[0] == "ATOM" and word[2] == "CA":
            type.append(word[3])
            index.append(word[2])
            x.append(float(word[6]))
            y.append(float(word[7]))
            z.append(float(word[8]))
    Total_atoms = int(len(type))
    print(Total_atoms)
    #print((word[3]))


    print("# Coarse grained molecule (1 bead per amino acid) in lammps data format \n " , file=out)
    print("\t %d atoms" %(len(index)), file=out)
    print("\t 0  bonds" , file=out)
    print("\t 0  angles" , file=out)
    print("\t 0  dihedrals" , file=out)
    print("\t 0  impropers \n" , file=out)
    print("Coord \n" , file=out)

    for i in range(len(type)):
        print("%d \t %5.5f \t %5.5f \t %5.5f" %(i+1, x[i], y[i], z[i]), file=out)

    print(" " , file=out)
    print("Types \n" , file=out)

    for i in range(len(type)):
        if type[i] == "ALA":
            print("%d \t 1" %(i+1), file=out)
        elif type[i] == "ARG":
            print("%d \t 2" %(i+1), file=out)
        elif type[i] == "ASN":
            print("%d \t 3" %(i+1), file=out)
        elif type[i] == "ASP":
            print("%d \t 4" %(i+1), file=out)
        elif type[i] == "GLU":
            print("%d \t 5" %(i+1), file=out)

        elif type[i] == "GLN":
            print("%d \t 6" %(i+1), file=out)
        elif type[i] == "GLY":
            print("%d \t 7" %(i+1), file=out)
        elif type[i] == "HIS":
            print("%d \t 8" %(i+1), file=out)
        elif type[i] == "ILE":
            print("%d \t 9" %(i+1), file=out)
        elif type[i] == "LEU":
            print("%d \t 10" %(i+1), file=out)

        elif type[i] == "LYS":
            print("%d \t 11" %(i+1), file=out)
        elif type[i] == "MET":
            print("%d \t 12" %(i+1), file=out)
        elif type[i] == "PHE":
            print("%d \t 13" %(i+1), file=out)
        elif type[i] == "PRO":
            print("%d \t 14" %(i+1), file=out)
        elif type[i] == "SER":
            print("%d \t 15" %(i+1), file=out)

        elif type[i] == "THR":
            print("%d \t 16" %(i+1), file=out)
        elif type[i] == "TRP":
            print("%d \t 17" %(i+1), file=out)
        elif type[i] == "TYR":
            print("%d \t 18" %(i+1), file=out)
        elif type[i] == "VAL":
            print("%d \t 19" %(i+1), file=out)
        elif type[i] == "CYS":
            print("%d \t 20" %(i+1), file=out)
    print(" ", file=out)
    print("Charges\n", file=out)

    for i in range(len(type)):
        print("%d \t 0" %(i+1), file=out)
        
pdb2lmp()
