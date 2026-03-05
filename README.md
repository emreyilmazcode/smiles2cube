# smiles2cube

A lightweight Python tool to generate **electron density .cube files** from SMILES strings.

Workflow:
- RDKit → Parse SMILES, add hydrogens, generate 3D conformer & MMFF optimize
- PySCF → Build molecule, run restricted Hartree-Fock (RHF), export density to Gaussian cube format

## Features
- Reproducible 3D embedding (fixed random seed = 42)
- Flexible basis set (default: sto-3g; better choices: 6-31g(d), def2-svp, cc-pvdz...)
- Returns total HF energy in Hartree
- Customizable cube grid resolution & PySCF verbosity

## Installation
```bash
pip install rdkit pyscf
