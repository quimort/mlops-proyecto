import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Datos simulados
data = pd.DataFrame({
    'fecha': ['2025-07-01', '2025-12-24', '2025-08-15', '2025-01-10', '2025-07-07'],
    'edad': [25, 34, 18, 60, 45],
    'clima': ['soleado', 'lluvioso', 'nublado', 'nevando', 'soleado'],
    'ir_sitio': [1, 0, 1, 0, 1]  # 1 = sí, 0 = no
})

# Preprocesar: convertir fecha a mes y clima a número
data['mes'] = pd.to_datetime(data['fecha']).dt.month
data['clima_cod'] = data['clima'].map({'soleado': 0, 'nublado': 1, 'lluvioso': 2, 'nevando': 3})

# Variables independientes y dependiente
X = data[['mes', 'edad', 'clima_cod']]
y = data['ir_sitio']

# Entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

# Predicción de ejemplo
nueva_fecha = '2025-07-15'
nueva_edad = 30
nuevo_clima = 'soleado'

nuevo_mes = pd.to_datetime(nueva_fecha).month
nuevo_clima_cod = {'soleado': 0, 'nublado': 1, 'lluvioso': 2, 'nevando': 3}[nuevo_clima]
#Preddicción
prediccion = modelo.predict([[nuevo_mes, nueva_edad, nuevo_clima_cod]])
print("¿Se puede ir al sitio?", "Sí" if prediccion[0] == 1 else "No")
