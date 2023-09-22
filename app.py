
import os
import sys
import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from TextSummarizer.pipeline.prediction import PredictionPipeline


text: str = "What is Text Summarization?"

app = FastAPI()


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Successful !!")

    except Exception as e:
        return Response(f"Error occurred during training \n{e}")


@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        res_text = obj.predict(text)
        return res_text

    except Exception as e:
        raise e


if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8080
                )