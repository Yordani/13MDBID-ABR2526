import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def visualizar_datos(fuente: str = 'data/raw/bank-additional-full.csv',
                     salida: str ='docs/figures/'):
        """ Genera una serie de gráfias sobre los datos y los exporta
        
    Args:
        fuente (str): Ruta al archivo CSV con los datos.
        salida (str): Ruta al directorio donde se guardarán las gráficas.
    """
        #gRAFICO 1: Distribución de la variable objetivo
        Path(salida).mkdir(parents=True, exist_ok=True)
        df = pd.read_csv(fuente, sep=';')
        plt.figure(figsize=(6, 4))
        sns.countplot(x='y', data=df)
        plt.title('Distribución de la variable objetivo (Suscripción a depósito a plazo)')
        plt.ylabel('Suscribio un depósito a plazo?')
        plt.xlabel('Cantidad de Clientes')
        plt.savefig(Path(salida) / 'Distribucion_target.png')
        plt.close()

        #Grafico 2: Distribución del nivel de educativo
        plt.figure(figsize=(6, 4))
        col = "education"
        order = df[col].value_counts().index
        sns.countplot(y=col, data=df, order=order)
        plt.title(f"Distribución de {col}")
        plt.xlabel("Cantidad")
        plt.ylabel(col)
        plt.savefig(Path(salida) / 'Distribucion_educacion.png')
        plt.close()

        #Grafico 3: Distribución del estado civil
        plt.figure(figsize=(6, 4))
        col = "marital"
        order = df[col].value_counts().index
        sns.countplot(y=col, data=df, order=order)
        plt.title(f"Distribución de {col}")
        plt.xlabel("Cantidad")
        plt.ylabel(col)
        plt.savefig(Path(salida) / 'Distribucion_marital.png')
        plt.close()

         #Grafico 4: Matriz de Correlación
        num_df = df.select_dtypes(include=['float64', 'int64'])
        corr = num_df.corr()
        plt.figure(figsize=(6, 4))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Matriz de correlaciones')
        plt.savefig(Path(salida) / 'matriz_correlacion.png')
        plt.close()


if __name__ == "__main__":
    visualizar_datos()
        

