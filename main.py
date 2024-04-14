from fastapi import fastAPI

app = fastAPI()

@app.get("/")
def inicio_mi_servidor():
    return ("Hola mundo")