from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

# ✅ Enable CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load the marks CSV into a DataFrame
df = pd.read_csv("marks.csv")

@app.get("/api")
def get_marks(name: list[str] = []):
    result = []
    for n in name:
        row = df[df["name"] == n]
        if not row.empty:
            result.append(int(row["marks"].values[0]))
        else:
            result.append(None)
    return JSONResponse(content={"marks": result})
