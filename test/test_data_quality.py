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

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")
    config._metadata['Proyecto'] = "13MBID - Metodologías de gestión"
    config._metadata['Autor'] = "Yordani Díaz"

if __name__ == "__main__":
    try:       
        test_esquema(datos_banco)
        test_basico(datos_banco)        
        with open("docs/test_results/test_results.txt", "w") as f:
            f.write("Todas las pruebas pasaron exitosamente.\n")
    except AssertionError as e:
         with open("docs/test_results/test_results.txt", "w") as f:
            f.write(f"Fallo en la prueba: {e}\n")
