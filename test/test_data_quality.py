import pandas as pd
from pandera.pandas import DataFrameSchema, Column
import pytest

@pytest.fixture
def datos_banco():
    df = pd.read_csv("data/raw/bank-additional-full.csv", sep=';')
    return df

def test_esquema(datos_banco):
    ''' Prueba para verificar que el DataFrame cumple con el esquema esperado '''
    df = datos_banco
    esquena = DataFrameSchema({
        "age": Column(int, nullable=False),
        "job": Column(str, nullable=False),
        "marital": Column(str, nullable=False),
        "education": Column(str, nullable=False),
        "default": Column(str, nullable=True),
        "housing": Column(str, nullable=False),
        "loan": Column(str, nullable=False),       
        "y": Column(str, nullable=False)
    })
    df = pd.read_csv('data/raw/bank-additional-full.csv', sep=';')

    esquena.validate(df)

def test_basico(datos_banco):
    ''' Prueba básica para verificar que el DataFrame no está vacío y tiene las columnas esperadas '''
    df = datos_banco

    #Verificar que el DataFrame no está vacío
    assert not df.empty, "El DataFrame está vacío"
    #verificar que no hay valores nulos
    assert df.isnull().sum().sum() == 0, "El DataFrame no contiene valores nulos"
    #Verificar que el DataFrame tiene el número esperado de columnas
    assert df.shape[1] == 21, "El DataFrame no tiene filas"


### TEST 3 – Valores permitidos en la columna 'marital'
def test_valores_marital(datos_banco):
    """Verifica que 'marital' solo contiene valores válidos"""
    df = datos_banco
    valores_validos = {"single", "married", "divorced", "unknown"}
    valores_encontrados = set(df["marital"].unique())
    assert valores_encontrados.issubset(valores_validos), \
        f"Valores no válidos en 'marital': {valores_encontrados - valores_validos}"

### TEST 4 – Valores permitidos en columnas binarias
def test_valores_binarios(datos_banco):
    """Verifica que columnas binarias contienen solo 'yes' o 'no' (y 'unknown' si aplica)"""
    df = datos_banco
    columnas = ["y", "loan", "housing", "default"]
    valores_validos = {"yes", "no", "unknown"}
    for col in columnas:
        valores_encontrados = set(df[col].unique())
        assert valores_encontrados.issubset(valores_validos), \
            f"Valores no válidos en '{col}': {valores_encontrados - valores_validos}"
        

if __name__ == "__main__":
    try:       
        test_esquema(datos_banco)
        test_basico(datos_banco)  
        test_valores_marital(datos_banco)
        with open("docs/test_results/test_results.txt", "w") as f:
            f.write("Todas las pruebas pasaron exitosamente.\n")
    except AssertionError as e:
         with open("docs/test_results/test_results.txt", "w") as f:
            f.write(f"Fallo en la prueba: {e}\n")
