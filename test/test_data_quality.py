import pandas as pd
from pandera.pandas import DataFrameSchema, Column
import pytest

@pytest.fixture
def datos_banco():
    df = pd.read_csv("data/raw/bank-additional-full.csv", sep=';')
    return df

def test_esquema():
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