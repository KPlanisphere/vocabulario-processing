# Vocabulario Processing Project

## Description
This project focuses on processing text files to extract and optimize vocabulary using Python and regular expressions. The main goal is to prepare the vocabulary for information retrieval tasks by performing several preprocessing steps, including tokenization, punctuation removal, conversion to lowercase, and filtering out short words. The project is built upon the results of previous laboratories and demonstrates advanced text processing techniques to enhance the efficiency of information retrieval within large text datasets.

### Files Included
- **lab4.py**: A Python script for processing text files to extract and optimize vocabulary.
- **Laboratorio 4 Vocabulario.pdf**: Official documentation detailing the objectives, methodology, and results of the project.
- **vocabularioReducidoT.txt**: A text file containing the reduced vocabulary.
- **vocabularioTruncado.txt**: A text file containing the truncated vocabulary.
- **documentos/documento-TRUNCADO.txt**: A sample processed document used in this project.

### Notable Code Snippets

#### 1. Function to Obtain Vocabulary
This function reads a text file and extracts unique words, filtering out numbers and converting the text to lowercase.

```python
import re

def obtener_vocabulario(archivo):
    with open(archivo, 'r') as f:
        texto = f.read()
        palabras = re.findall(r'\b(?![0-9]+\b)\w+\b', texto.lower())
        return set(palabras)
```

#### 2. Processing Text Files

This snippet processes all text files in the specified directory to extract and optimize vocabulary.

```python
import os

# Directory containing text files
directorio = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab4\documentos'
output_file_final = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab4\vocabularioReducidoT.txt'

# Set to store the total vocabulary
vocabulario_total = set()

# Process each text file in the directory
for archivo in os.listdir(directorio):
    if archivo.endswith('.txt'):
        ruta_archivo = os.path.join(directorio, archivo)
        vocabulario_archivo = obtener_vocabulario(ruta_archivo)
        vocabulario_total.update(vocabulario_archivo)

# Sort the vocabulary alphabetically
vocabulario_ordenado = sorted(vocabulario_total)

# Filter out words with 2 characters or less
vocabulario_filtrado = [palabra for palabra in vocabulario_ordenado if len(palabra) > 2]

# Write the filtered vocabulary to the output file
with open(output_file_final, 'w') as f:
    for palabra in vocabulario_filtrado:
        f.write(palabra + '\n')
```

### Official Documentation Summary

The official documentation provided in "Laboratorio 4 Vocabulario.pdf" outlines the following key points:

#### Objectives

-   Develop a Python script to extract and optimize the vocabulary of a given document.
-   Perform preprocessing steps including tokenization, punctuation removal, conversion to lowercase, and truncation of words.
-   Create a reduced vocabulary by filtering out terms with two or fewer letters.

#### Methodology

1.  **Vocabulary Extraction**: Extract unique words from text files, excluding numbers and converting text to lowercase.
2.  **Vocabulary Optimization**: Filter out words with two characters or fewer to create a reduced vocabulary.
3.  **Alphabetical Sorting**: Sort the vocabulary alphabetically for better organization and readability.

#### Results and Discussion

-   The initial vocabulary extracted contains many terms, including short words with only two letters.
-   The reduced vocabulary, which excludes words with two letters or fewer, shows a significant decrease in the number of terms.
-   The reduced vocabulary improves the efficiency of information retrieval tasks by focusing on more meaningful terms.

#### Conclusion

The project successfully demonstrates advanced text processing techniques to optimize vocabulary for information retrieval tasks. The reduction in vocabulary size by filtering out short words enhances the efficiency and relevance of the retrieved information.

### Installation and Usage

1.  Clone the repository to your local machine.
2.  Ensure you have Python installed.
3.  Run the `lab4.py` script to process the text files and extract the optimized vocabulary.

```bash
git clone https://github.com/KPlanisphere/vocabulario-processing.git
cd vocabulario-processing
python lab4.py
```

### Dependencies

-   Python
