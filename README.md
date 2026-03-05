# smiles2cube

A lightweight Python tool that generates **electron density .cube files** from SMILES strings.

**Workflow**:
1. RDKit parses the SMILES → adds hydrogens → generates 3D conformer (ETK) → MMFF optimizes geometry
2. PySCF builds the molecule from RDKit coordinates
3. Runs restricted Hartree-Fock (RHF) calculation
4. Exports the electron density to Gaussian cube format using cubegen

## Features
- Reproducible 3D embedding (fixed random seed = 42)
- Flexible basis set support (default: sto-3g; recommend 6-31g(d), def2-svp, cc-pvdz...)
- Returns total HF energy in Hartree
- Customizable cube grid resolution and PySCF verbosity

## Installation
```bash
pip install rdkit pyscf
