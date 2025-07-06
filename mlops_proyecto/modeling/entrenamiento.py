import mlflow

mlflow.set_experiment("experimento-demo")

with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_metric("accuracy", 0.92)
