from tkinter import Scale

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
app = FastAPI()

@app.get("/shipment/{id}")
def get_shipments(id: int|float):
    return {
        "content":"wooden table",
        "status":"In progress"
    }
@app.get("/scalar_docs", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )
