from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import json
import os

app = FastAPI(title="FastAPI + C++ AI Model")

CPP_BINARY = "./cpp_model/build/model_runner"

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(req: PromptRequest):
    try:
        result = subprocess.run(
            [CPP_BINARY, req.prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)
