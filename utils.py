import pandas as pd 
import rdkit
import cirpy

path = "Data/smell_1.csv"

def read_csv_2df(path):
    """
    Reads a CSV file and prints each row to the console.

    Args:
        file_path (str): The path to the CSV file to be read.

    Returns:
        pandas.DataFrame: A DataFrame containing the data from the CSV file.
        
    """
    df = pd.read_csv(path, sep = ";", index_col = False)
    
    if isinstance(df.mol_frac[1], str):
        df['mol_frac'] = df['mol_frac'].str.replace(',', '.').astype(float)
    return df


def filter_zero_molfrac(df):
    """
    Reads a DataFrame and return a new data frame only with entries where mol_frac col > 0.

    Args:
        df (pandas.DataFrame: The path to the CSV file to be read.

    Returns:
        pandas.DataFrame: A DataFrame containing lines where mol_frac is greater than 0.
        
    """
    is_mol_frac_gtzero = df.mol_frac > 0.0
    return df.loc[is_mol_frac_gtzero, :]


def cas_to_smiles(CAS):
    smiles = cirpy.resolve(CAS, 'smiles')
    return smiles
 

     
     
     
     



