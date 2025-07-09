# estudiantes entrega
```
Quim Ortuño
Freddy Vargas
Joaquim Balletbo
```

# mlops-proyecto

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This is ana analisis of data

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         mlops_proyecto and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── mlops_proyecto   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes mlops_proyecto a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------


## 🧪 Requisitos e instalación

Clona el repositorio y crea un entorno virtual:

```bash
git clone https://github.com/tu-usuario/mlops-proyecto.git
cd mlops-proyecto


pipenv install -dev

pipenv shell


# Inicializa DVC (solo la primera vez)
dvc init

# Agrega un archivo de datos al control de DVC
dvc add [airline_data.csv](http://_vscodecontentref_/11)

# Guarda los cambios en git
git add data/raw/airline_data.csv.dvc .gitignore
git commit -m "Track airline_data.csv with DVC"

# Para recuperar datos versionados
dvc pull


# Ejecuta un experimento de entrenamiento
python [entrenamiento.py](http://_vscodecontentref_/12)

# Inicia la interfaz de usuario de MLflow para visualizar experimentos
mlflow ui