import pandas as pd
import numpy as np

INPUT_CSV = 'data/raw/bank-additional-full.csv'
OUTPUT_CSV = 'data/processed/bank-processed-full.csv'

def preprocess_data(input_path=INPUT_CSV, output_path=OUTPUT_CSV):
    # Load the dataset
    df = pd.read_csv(input_path, sep=';')
    
    #Adactar nombres de columnas
    df.columns = df.columns.str.replace('-', '_')

    # transformar valores 'unknown' a NaN
    df.replace('unknown', pd.NA, inplace=True)

    #se hace filtro para eliminar filas con valores desconocidos en la columna 'job'
    df.drop(columns=['default'], inplace=True)
    
    #se eliminan filas con valores nulos
    df.dropna(inplace=True)

    #se eliminan filas duplicadas
    df.drop_duplicates(inplace=True)

    #save the processed dataset
    df.to_csv(output_path, index=False)

    return df.shape

if __name__ == "__main__":
    dimenciones = preprocess_data()
    with open('data/processed/transformations.txt', 'w') as f:
        f.write("Transformaciones realizadas \n")
        f.write("Se remplazaron los valores 'unknown' por NaN \n")
        f.write("Se eliminaron las filas con valores nulos \n")
        f.write("Se eliminaron las filas duplicadas\n")
        f.write(f"Se eliminó la columna 'default' debido a las alta cantidad de valores nulos \n")
        f.write(f"Cantidad de filas finales: {dimenciones[0]}.\n")
        f.write(f"Cantidad de columnas finales: {dimenciones[1]}.\n")