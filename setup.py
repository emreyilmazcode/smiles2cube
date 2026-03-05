from setuptools import setup

setup(
    name='smiles2cube',
    version='0.1.0',
    author='Emre Yılmaz',
    author_email='eyilmaz18@icloud.com',
    description='Generate electron density cubes from SMILES strings.',
    url='https://github.com/emreyilmazcode/smiles2cube',
    py_modules=['smiles2cube'],
    install_requires=[
        'rdkit',
        'pyscf'
    ],
    python_requires='>=3.6',
)
