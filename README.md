# Project Title: Impatto del benessere psicologico degli studenti sul loro rendimento accademico

## Overview
Attraverso un'analisi dei dati relativi alle prestazioni accademiche e alle condizioni psicologiche degli studenti, si vogliono identificare correlazioni tra salute mentale e successo o fallimento accademico. Questo consentirà di sviluppare interventi mirati per migliorare il benessere complessivo degli studenti.


## Installation and Setup
Instructions on setting up the project environment:
1. Clone the repository: `git clone https://github.com/DeliaCavalca/AI_Project.git`
2. Install dependencies: `pip install -r requirements.txt`

## Data

**Raw Data**

Dati raccolti attraverso un questionario somministrato a studenti di differenti corsi di laurea dell'Università degli Studi di Bologna.
Tali dati presentano una serie di informazioni relative alla condizione psicologica e al percorso accademico degli studenti, oltre ad altre informazioni non di nostro interesse.

**Processed Data**

Sono state rimosse le informazioni non di nostro interesse. 
Data preprocessing: i dati sono stati puliti e normalizzati, in modo da poter essere in seguito analizzati.
Nello specifico, abbiamo gestito: valori mancanti, valori incoerenti, formato dei valori.

**Results Data**

Risultati salvati: dai differenti test di clustering sono stati salvati i risultati di nostro interesse, ovvero media e varianza calcolate per ogni feature di ogni cluster individuato.
I dati sono raccolti in cartelle differenti (una per ogni algoritmo utilizzato). All'interno di una singola cartella, sono presenti i differenti test svolti sui diversi dataset (ad esempio: output_1A.xlsx si riferisce al test A svolto sul subset_1).

## Usage
How to run the project:
1. Spostarsi all'interno della cartella coi sorgenti `/src/scripts`
2. Scegliere la tipologia di clustering da eseguire, ad esempio KMEANS clustering
3. Impostare nel relativo .py file (es. `1_kmeans.py`) il dataset sul quale si vuole fare il clustering (es. `subset_3.xlsx`) e un adeguato nome per il file dei risultati (es. `output_3C.xlsx`)
4. Eseguire il clustering: `py 1_kmeans.py`
5. Analizzare i risultati: `py 1_kmeans_analysis.py '../../data/results/outputKMEANS/output_3C.xlsx'`

How to test multiple algorithms:
1. Spostarsi all'interno della cartella coi file di testing `/tests`
2. Scegliere uno dei file di testing da eseguire
4. Eseguire lo script: `py fileName.py`


## Structure
- `/data`: Contains raw, processed and results data.
- `/src`: Source code for the project.
  - `/scripts`: Individual scripts or modules.
  - `/notebooks`: Jupyter notebooks or similar.
- `/tests`: Test cases for your application.
- `/docs`: Additional documentation in text format (e.g., LaTeX or Word).
- `/public`: Folder where GitLab pages will write static website. 
- `index.html`: Documentation in rich format (e.g., HTML, Markdown, JavaScript), will populate `public`.

## Contribution
Guidelines for contributing to the project (if applicable).

## License
State the license or leave it as default (if applicable).

## Contact
Delia Cavalca - delia.cavalca@studio.unibo.it

Claudia Brunetti - claudia.brunetti4@studio.unibo.it
