from fastapi import FastAPI

app = FastAPI(title="RAG Knowledge API")

@app.get("/")
def root():
    return {"message": "RAG Pipeline Running"}