from fastapi import FastAPI
import asyncio
import os
import uvicorn

app = FastAPI()

delay_seconds = float(os.getenv("DELAY_MS", "0"))/1000

@app.get("/health")
async def health():
    await asyncio.sleep(delay_seconds)
    return {"status": "ok"}

@app.get("/sum")
async def sum_get(a: int, b: int):
    await asyncio.sleep(delay_seconds)
    return {"sum": a + b}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)