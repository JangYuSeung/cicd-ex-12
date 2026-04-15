from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "fastapi"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI!"}