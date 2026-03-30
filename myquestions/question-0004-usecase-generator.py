from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import matthews_corrcoef
from sklearn.datasets import make_classification
import random


def generar_caso_de_uso_evaluar_clasificador_mcc():
    """
    Genera un caso de prueba aleatorio para evaluar_clasificador_mcc
    """
    
    n_samples = random.randint(200, 400)
    
    X, y = make_classification(
        n_samples=n_samples,
        n_features=10,
        weights=[0.85, 0.15],
        random_state=42
    )
    
    test_size = random.uniform(0.2, 0.3)
    
    # -------------------------
    # INPUT
    # -------------------------
    input_data = {
        "X": X.copy(),
        "y": y.copy(),
        "test_size": test_size
    }
    
    # -------------------------
    # OUTPUT (GROUND TRUTH)
    # -------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    
    mcc = matthews_corrcoef(y_test, y_pred)
    
    output_data = mcc
    
    return input_data, output_data

# --- Ejemplo de uso ---
if __name__ == "__main__":
    entrada, salida_esperada = generar_caso_de_uso_evaluar_clasificador_mcc()
    
    print("=== INPUT (Diccionario) ===")
    print(f"Shape de X: {entrada['X'].shape}")
    print(f"Shape de y: {entrada['y'].shape}")
    print(f"test_size: {entrada['test_size']:.2f}")
    
    print("\n=== OUTPUT ESPERADO ===")
    print(f"Valor MCC: {salida_esperada}")