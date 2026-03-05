# smiles2cube
[<image-card alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" ></image-card>](https://opensource.org/licenses/MIT)
[<image-card alt="Python 3.8+" src="https://img.shields.io/badge/python-3.8+-blue.svg" ></image-card>](https://www.python.org/downloads/)

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

## 🚀 Installation

You can install `smiles2cube` directly from PyPI using pip. Required dependencies (`rdkit` and `pyscf`) will be installed automatically.

pip install smiles2cube

## Usage
from smiles2cube import smiles_to_cube

# Ethanol example with better basis
energy = smiles_to_cube(
    smiles="CCO",
    output_file="ethanol_density.cube",
    basis="6-31g(d)",
    grid_resolution=(100, 100, 100),   # optional
    verbose=4                           # optional: more output
)

print(f"Total HF energy: {energy:.8f} Hartree")
