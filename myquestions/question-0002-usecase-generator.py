import pandas as pd
import numpy as np
def generar_caso_de_uso_detectar_discrepancias_inventario():
    n_productos = np.random.randint(10, 20)
    stock_ini = np.random.randint(100, 500, size=n_productos)
    ventas = np.random.randint(0, 100, size=n_productos)
    # Introducir errores aleatorios en el stock final real
    stock_real = (stock_ini - ventas) + np.random.choice([0, 5, -10, 0, 0], size=n_productos)
    
    df = pd.DataFrame({
        "producto_id": range(n_productos),
        "stock_inicial": stock_ini,
        "ventas": ventas,
        "stock_final_real": stock_real
    })
    
    umbral = 2
    # El stock_final_esperado es stock_ini - ventas. La discrepancia es abs(real - esperado)
    diff = np.abs(df["stock_final_real"] - (df["stock_inicial"] - df["ventas"]))
    output = df[diff > umbral].copy()
    output["discrepancia"] = diff[diff > umbral]
    output = output.sort_values(by="discrepancia", ascending=False)
    
    return {"df": df, "umbral_error": umbral}, output

# --- Ejemplo de uso ---
if __name__ == "__main__":
    entrada, salida_esperada = generar_caso_de_uso_detectar_discrepancias_inventario()
    
    print("=== INPUT (Diccionario) ===")
    print(f"umbral_error: {entrada['umbral_error']}")
    print("DataFrame (primeras 5 filas):")
    print(entrada['df'].head())
    
    print("\n=== OUTPUT ESPERADO ===")
    print("Productos con discrepancias:")
    print(salida_esperada.head())