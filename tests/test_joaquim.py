import mlflow
import time
import random


with mlflow.start_run():

    mlflow.log_param("model_type", "dummy‑regressor")
    mlflow.log_param("seed", 42)


    for epoch in range(3):
        loss = random.random() 
        mlflow.log_metric("loss", loss, step=epoch)
        time.sleep(0.5)

    with open("output.txt", "w") as f:
        f.write(f"Final loss: {loss:.4f}\n")
    mlflow.log_artifact("output.txt")
