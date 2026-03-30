import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_identificar_usuarios_constantes():
    """
    Genera un caso de prueba aleatorio para identificar_usuarios_constantes
    """
    
    n_usuarios = random.randint(5, 10)
    data = []
    
    min_dias = random.randint(2, 4)
    
    for uid in range(n_usuarios):
        tiene_racha = random.choice([True, False])
        
        if tiene_racha:
            racha_len = random.randint(min_dias, min_dias + 2)
            fechas = pd.date_range(start="2026-01-01", periods=racha_len).tolist()
        else:
            # Fechas no consecutivas
            fechas = pd.to_datetime(
                np.random.choice(pd.date_range("2026-01-01", periods=10), size=3, replace=False)
            )
        
        for f in fechas:
            data.append({"usuario_id": uid, "fecha": f})
    
    df = pd.DataFrame(data)
    
    # -------------------------
    # INPUT
    # -------------------------
    input_data = {
        "df": df.copy(),
        "min_dias_consecutivos": min_dias
    }
    
    # -------------------------
    # OUTPUT (GROUND TRUTH)
    # -------------------------
    df_sorted = df.copy()
    df_sorted["fecha"] = pd.to_datetime(df_sorted["fecha"])
    df_sorted = df_sorted.sort_values(by=["usuario_id", "fecha"])
    
    usuarios_validos = []
    
    for uid, grupo in df_sorted.groupby("usuario_id"):
        fechas = grupo["fecha"].sort_values()
        diffs = fechas.diff().dt.days
        
        racha = 1
        max_racha = 1
        
        for d in diffs[1:]:
            if d == 1:
                racha += 1
                max_racha = max(max_racha, racha)
            else:
                racha = 1
        
        if max_racha >= min_dias:
            usuarios_validos.append(uid)
    
    output_data = sorted(usuarios_validos)
    
    return input_data, output_data

# --- Ejemplo de uso ---
if __name__ == "__main__":
    entrada, salida_esperada = generar_caso_de_uso_identificar_usuarios_constantes()
    
    print("=== INPUT (Diccionario) ===")
    print(f"min_dias_consecutivos: {entrada['min_dias_consecutivos']}")
    print("DataFrame (primeras 5 filas):")
    print(entrada['df'].head())
    
    print("\n=== OUTPUT ESPERADO ===")
    print("Usuarios con racha suficiente:")
    print(salida_esperada)