from rdkit import Chem
from rdkit.Chem import AllChem
from pyscf import gto, scf, tools


def smiles_to_cube(smiles: str, output_file: str = "density.cube", basis: str = "sto-3g") -> float:
    """
    SMILES dizisinden elektron yoğunluğu cube dosyası üretir.

    Args:
        smiles:      Molekülün SMILES gösterimi
        output_file: Çıktı cube dosyasının adı (varsayılan: density.cube)
        basis:       Kullanılacak basis seti (varsayılan: sto-3g)

    Returns:
        Toplam HF enerjisi (Hartree cinsinden)
    """
    # 1. RDKit ile 3D geometri oluştur ve optimize et
    mol_rd = Chem.MolFromSmiles(smiles)
    if mol_rd is None:
        raise ValueError(f"Geçersiz SMILES dizisi: {smiles!r}")

    mol_rd = Chem.AddHs(mol_rd)
    result = AllChem.EmbedMolecule(mol_rd, randomSeed=42)
    if result != 0:
        raise RuntimeError("3D geometri oluşturulamadı. SMILES'i kontrol edin.")

    AllChem.MMFFOptimizeMolecule(mol_rd)

    # 2. PySCF atom listesini oluştur
    conf = mol_rd.GetConformer()
    atom_list = []
    for i in range(mol_rd.GetNumAtoms()):
        symb = mol_rd.GetAtomWithIdx(i).GetSymbol()
        pos  = conf.GetAtomPosition(i)
        atom_list.append((symb, (pos.x, pos.y, pos.z)))

    # 3. PySCF ile Hartree-Fock hesabı yap
    mol_pyscf = gto.M(atom=atom_list, basis=basis, verbose=3)
    mf = scf.RHF(mol_pyscf)
    energy = mf.kernel()

    print(f"\n✅ Toplam HF enerjisi: {energy:.8f} Hartree")

    # 4. Elektron yoğunluğunu cube dosyasına yaz
    dm = mf.make_rdm1()
    tools.cubegen.density(mol_pyscf, output_file, dm)
    print(f"✅ Cube dosyası kaydedildi: {output_file}")

    return energy
