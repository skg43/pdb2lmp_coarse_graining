# PDB to LAMMPS Coarse-Grained Data File Converter

This project provides a Python script that converts an all-atom crystallographic protein structure (PDB file) into a coarse-grained LAMMPS data file.  
It places a single coarse-grained bead at each C-alpha (Cα) atom position, simplifying the structure for coarse-grained molecular dynamics simulations.

---

## 📚 Project Description

Coarse-grained modeling is a powerful technique to study large biomolecular systems efficiently.  
This script automates the conversion of full-atomistic PDB structures into coarse-grained representations by:

- Extracting C-alpha atom positions from the input PDB file.
- Writing a simplified LAMMPS-format data file suitable for coarse-grained simulations.
- Reducing computational complexity while preserving the protein's backbone topology.

---

## 📂 Repository Structure

```
pdb2lmp/
├── 2qna.pdb               # Example input PDB structure file
├── kapB_lmp_mol.data       # Example output coarse-grained LAMMPS data file
├── pdb_2_lmp.py            # Python script for PDB to coarse-grained LAMMPS conversion
└── README.md               # Project overview and usage instructions
```

---

## 🚀 How to Run

1. Make sure you have Python installed (version 3.x recommended).

2. Place your PDB file in the working directory.

3. Run the script:
   ```bash
   python pdb_2_lmp.py
   ```

4. The script will generate a `.data` file containing C-alpha beads only, ready for use in LAMMPS.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Developed By

Sanjeev Kumar Gautam
