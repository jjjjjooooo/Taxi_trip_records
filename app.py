import os
import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse

app = FastAPI()

text: str = "Average Trip Length for Yellow Taxis in NYC"


@app.get("/", tags=["Authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/analysis", tags=[text])
async def analysis():
    try:
        os.system("python main.py")
        return "Analysis is successfully carried out!!"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error Occurred! {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
