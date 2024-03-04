# import libraries
import pandas as pd
import numpy as np

# load dataset
dataset = pd.read_excel('../../data/processed/dataset.xlsx')


# check the first few rows of the dataset
print(dataset.head())
# check num of rows and columns
print(f"\nThe dataset has {dataset.shape[0]} rows and {dataset.shape[1]} columns.\n")
print("------------------------")



# ------------------------------------------------------
# ------------------------------------------------------
# DATA PREPROCESSING

# remove rows with null value in a specific col
dataset = dataset.dropna(subset=['CDL'])
dataset = dataset.dropna(subset=['SODD'])
dataset = dataset.dropna(subset=['VOTO_DIPLOMA'])

# print only rows with null value in a specific col
#print(dataset.loc[dataset['VOTO_DIPLOMA'].isnull()])

# check for missing values
print("\nCOL WITH MISSING VALUES\n")
print(dataset.isnull().sum())
print("------------------------")


# check column: ETA
# ------------------------------------------------------
def checkEta():
    #print(dataset['ETA'].unique().tolist())
    #print("------------------------")

    # convert into number
    dataset['ETA'] = pd.to_numeric(dataset['ETA'], errors='coerce')

    # accepted values: 18 - 50
    accepted_val = dataset[(dataset['ETA'] >= 18) & (dataset['ETA'] <= 50)]['ETA']
    mean_val = accepted_val.mean().round(0)
    #print("MEAN VAL ETA: ", mean_val)
    # substitute nan or incorrect val with the mean val
    dataset.loc[(dataset['ETA'].isnull()) | ((dataset['ETA'] < 18) | (dataset['ETA'] > 50)), 'ETA'] = mean_val
checkEta()
# ------------------------------------------------------


# check column: VOTO_DIPLOMA
# ------------------------------------------------------
def checkVoto():
    #print(dataset['VOTO_DIPLOMA'].unique().tolist())
    #print("------------------------")

    # convert values from scale 0-60 into scale 0-100 (only if the valeue contains "/60")
    dataset.loc[dataset['VOTO_DIPLOMA'].str.contains('/60', na=False), 'VOTO_DIPLOMA'] = (pd.to_numeric(dataset['VOTO_DIPLOMA'].str.split('/').str[0], errors='coerce') / 60) * 100
    dataset.loc[dataset['VOTO_DIPLOMA'].str.contains('su 60', na=False), 'VOTO_DIPLOMA'] = (pd.to_numeric(dataset['VOTO_DIPLOMA'].str.split(' su').str[0], errors='coerce') / 60) * 100
    dataset['VOTO_DIPLOMA'] = dataset['VOTO_DIPLOMA'].astype(str)

    # replace values of the form "x/100" with just "x"
    dataset['VOTO_DIPLOMA'] = dataset['VOTO_DIPLOMA'].str.split('/').str[0]
    # replace anything that's not a number or a dot with an empty string
    dataset['VOTO_DIPLOMA'] = dataset['VOTO_DIPLOMA'].str.replace(',', '.')
    dataset['VOTO_DIPLOMA'] = dataset['VOTO_DIPLOMA'].str.replace('[^\d.]', '', regex=True)

    # convert into number
    dataset['VOTO_DIPLOMA'] = pd.to_numeric(dataset['VOTO_DIPLOMA'], errors='coerce')
    dataset['VOTO_DIPLOMA'] = dataset['VOTO_DIPLOMA'].round(2)

    # get only values between 60 and 100
    accepted_val = dataset[(dataset['VOTO_DIPLOMA'] >= 60) & (dataset['VOTO_DIPLOMA'] <= 100)]['VOTO_DIPLOMA']
    mean_val = accepted_val.mean().round(2)
    #print("MEAN VAL: ", mean_val)

    # substitute nan or incorrect val with the mean val
    dataset.loc[(dataset['VOTO_DIPLOMA'].isnull()) | ((dataset['VOTO_DIPLOMA'] < 60) | (dataset['VOTO_DIPLOMA'] > 100)), 'VOTO_DIPLOMA'] = mean_val
checkVoto()
# ------------------------------------------------------

# check column: N_ESAMI
# ------------------------------------------------------
def checkEsami():
    #print(dataset['N_ESAMI'].unique().tolist())
    #print("------------------------")

    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('Tutti, ho completato il mio piano di studi (16)', '16', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.split('/').str[0]
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.split(' ').str[0]
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.split('+').str[0]
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('Otto', '8', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('Quattro', '4', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('Tre', '3', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('Due', '2', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('due', '2', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('Cinque', '5', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('Sei', '6', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('Sette', '7', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('Dieci', '10', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('Zero', '0', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('Nessuno', '0', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('nessun', '0', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('nessuno', '0', regex=True)
    
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.replace('[^\d.]', '', regex=True)
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.split('.').str[0]
    dataset['N_ESAMI'] = dataset['N_ESAMI'].str.split(',').str[0]
    
    # convert into number
    dataset['N_ESAMI'] = pd.to_numeric(dataset['N_ESAMI'], errors='coerce')

    mean_val = dataset['N_ESAMI'].mean().round(0)
    #print("MEAN VAL: ", mean_val)

    # substitute nan or incorrect val with the mean val
    dataset.loc[(dataset['N_ESAMI'].isnull()) | ((dataset['N_ESAMI'] > 80)), 'N_ESAMI'] = mean_val

    #print(dataset['N_ESAMI'].unique().tolist())
    #print("------------------------")
checkEsami()
# ------------------------------------------------------


# check column: NON_SUPERATI
# ------------------------------------------------------
def checkNonSuperati():
    #print(dataset['NON_SUPERATI'].unique().tolist())
    #print("------------------------")

    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('Un paio', '2', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('Due esami, un tentativo per uno', '2', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('2 o 3', '2', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('0 o 1', '1', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('3 volte su 5', '3', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('dalle 4 alle 7 volte', '5', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('7 +1 idoneità', '7', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('Zero', '0', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('Mai', '0', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('May', '0', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('mai', '0', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('Nessuna', '0', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('Nessuno', '0', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('nessuna', '0', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('primo', '0', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('Uno', '1', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('Una volta', '1', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('una', '1', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('due', '2', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('Due', '2', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('Sei', '6', regex=True)
    
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.split('/').str[0]
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.split('-').str[0]

    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.replace('[^\d.]', '', regex=True)
    dataset['NON_SUPERATI'] = dataset['NON_SUPERATI'].str.split('.').str[0]

    # convert into number
    dataset['NON_SUPERATI'] = pd.to_numeric(dataset['NON_SUPERATI'], errors='coerce')

    mean_val = dataset['NON_SUPERATI'].mean().round(0)
    #print("MEAN VAL: ", mean_val)

    # substitute nan or incorrect val with the mean val
    dataset.loc[(dataset['NON_SUPERATI'].isnull()) | ((dataset['NON_SUPERATI'] > 20)), 'NON_SUPERATI'] = mean_val


    #print(dataset['NON_SUPERATI'].unique().tolist())
    #print("------------------------")
checkNonSuperati()
# ------------------------------------------------------


# check column: RISOSTENUTI
# ------------------------------------------------------
def checkRisostenuti():
    #print(dataset['RISOSTENUTI'].unique().tolist())
    #print("------------------------")

    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('architetture degli elaboratori', '1', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Il voto ottenuto mi ha sempre soddisfatto', '0', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Ne ho fatto 1 che ho superato con 22', '1', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('15 superati', '', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('19/20', '', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('13 e 1', '1', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('21 blocchi di esami e risostenuto 1', '1', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('1-30', '1', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('3,1', '1', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('14 0 risostenuti', '0', regex=True)

    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Mai', '0', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('mai', '0', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('O', '0', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Nessuno', '0', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('nessuno', '0', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Nessuna', '0', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Nesuuno', '0', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Zero', '0', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('zero', '0', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Uno', '1', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('uno', '1', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Una', '1', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Due', '2', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Dieci', '10', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('Quattro', '4', regex=True)
    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('-', '0', regex=True)

    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.split('/').str[0]

    dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.replace('[^\d.]', '', regex=True)
    #dataset['RISOSTENUTI'] = dataset['RISOSTENUTI'].str.split('.').str[0]

    # convert into number
    dataset['RISOSTENUTI'] = pd.to_numeric(dataset['RISOSTENUTI'], errors='coerce')

    mean_val = dataset['RISOSTENUTI'].mean().round(0)
    #print("MEAN VAL: ", mean_val)

    # substitute nan or incorrect val with the mean val
    dataset.loc[(dataset['RISOSTENUTI'].isnull()) | ((dataset['RISOSTENUTI'] > 19)), 'RISOSTENUTI'] = mean_val


    #print(dataset['RISOSTENUTI'].unique().tolist())
    #print("------------------------")
checkRisostenuti()
# ------------------------------------------------------


# check column: MEDIA_VOTI
# ------------------------------------------------------
def checkMedia():
    #print(dataset['MEDIA_VOTI'].unique().tolist())
    #print("------------------------")

    dataset['MEDIA_VOTI'] = dataset['MEDIA_VOTI'].str.split('/').str[0]
    dataset['MEDIA_VOTI'] = dataset['MEDIA_VOTI'].str.replace(',', '.', regex=True)
    dataset['MEDIA_VOTI'] = dataset['MEDIA_VOTI'].str.replace('[^\d.]', '', regex=True)

    # convert into number
    dataset['MEDIA_VOTI'] = pd.to_numeric(dataset['MEDIA_VOTI'], errors='coerce')

    mean_val = dataset['MEDIA_VOTI'].mean().round(2)
    #print("MEAN VAL: ", mean_val)

    # substitute nan or incorrect val with the mean val
    dataset.loc[((dataset['MEDIA_VOTI'].isnull()) | (dataset['MEDIA_VOTI'] < 18) | (dataset['MEDIA_VOTI'] > 30)), 'MEDIA_VOTI'] = mean_val

    #print(dataset['MEDIA_VOTI'].unique().tolist())
    #print("------------------------")
checkMedia()
# ------------------------------------------------------


# column control where null values ​​must be replaced with the average of the column itself
# ------------------------------------------------------
def checkColonne(dataset):
    array_colonne=["MOT_INTR", "MOT_ES", "MOT_ID", "MOT_INTRO", "AMOT", "LOC_INT", "IIS_INTDOC", "IIS_ATT", "IIS_PARI", "IIS_SVACC", "IIS_IMP1", 
                   "IIS_IMP2", "RIC_IMP", "REGOLAZIONE_EMOTIVA", "TEAM", "AUT_ACC", "RISP_SCA","CH_CARR","RIC_CARR", "TASK_CRA", "AUT_CAR"]
    for colonna in array_colonne:
            # Converts cells in the specified column to numbers
            dataset[colonna] = pd.to_numeric(dataset[colonna], errors='coerce')
            
            # Calculate the average value of the "colonna" column excluding null values
            media = dataset[colonna].mean(skipna=True).round(0)
            #print("Media nella colonna", colonna, ":", media)
            
            valori_nulli = dataset[colonna ].isnull().sum()
            #print("Numero di valori nulli PRIMA in ", colonna, ":", valori_nulli)
        
            # Replace null values in the "colonna" column with the calculated mean
            dataset[colonna].fillna(media, inplace=True)
            
            #Set all values with 0 values after the decimal point 
            dataset[colonna] =dataset[colonna].round(0)
            
            valori_nulli = dataset[colonna].isnull().sum()
            #print("Numero di valori nulli DOPO", colonna, ":", valori_nulli)
checkColonne(dataset)

# ------------------------------------------------------
# ------------------------------------------------------
# UPDATE DATASET
#dataset.to_excel('dataset_cleaned.xlsx', index=False)

# ------------------------------------------------------
# ------------------------------------------------------
# SEPARATE DATASET

dataset = pd.read_excel('../../data/processed/dataset_cleaned.xlsx')

# iterate on col "ANNO"
for anno_value in dataset['ANNO'].unique():
    # select rows in dataset with 'anno_value'
    subset = dataset[dataset['ANNO'] == anno_value]
    
    # save the subset in a new file CSV
    subset.to_excel(f"subset_{anno_value}.xlsx", index=False)

