import pandas as pd

def test_great_expectations():
    ''' Prueba para verificar que el DataFrame cumple con las expectativas definidas en Great Expectations '''
    
    # Cargar el DataFrame
    df = pd.read_csv("data/raw/bank-additional-full.csv", sep=';')

   # Validar las expectativas
    results = {
        "success": True,
        "expectations": [],
        "statistics": {"success_count": 0, "total_count": 0}
    }

    def add_expectation(expectation_name, condition, message=""):
        results["statistics"]["total_count"] += 1
        if condition:
            results["statistics"]["success_count"]  += 1
            results["expectations"].append({
                    "expectation": expectation_name,
                    "success": True
            })
        else:
            results["success"] = False
            results["expectations"].append({
                    "expectation": expectation_name,
                    "success": False,
                    "message": message
             })
            
    add_expectation(
        "age_range",
        df["age"].between(18, 100).all()
    )
    
    add_expectation(
        "target_values",
        df["y"].isin(['yes', 'no']).all()
    )
    