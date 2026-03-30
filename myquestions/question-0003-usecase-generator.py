from sklearn.datasets import make_classification
from sklearn.decomposition import KernelPCA
from sklearn.cluster import KMeans
import random

def generar_caso_de_uso_reducir_y_agrupar_kernel():
    """
    Genera un caso de prueba aleatorio para reducir_y_agrupar_kernel
    """
    
    n_samples = random.randint(50, 100)
    
    # Aseguramos consistencia
    n_features = random.randint(4, 6)
    n_informative = random.randint(2, n_features - 1)
    
    X, _ = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=n_informative,
        n_redundant=0,   
        n_repeated=0,    
        random_state=42
    )
    
    n_clusters = random.randint(2, 4)
    
    # -------------------------
    # INPUT
    # -------------------------
    input_data = {
        "X": X.copy(),
        "n_clusters": n_clusters
    }
    
    # -------------------------
    # OUTPUT (GROUND TRUTH)
    # -------------------------
    kpca = KernelPCA(n_components=2, kernel='rbf')
    X_reduced = kpca.fit_transform(X)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(X_reduced)
    
    output_data = (kpca, labels)
    
    return input_data, output_data