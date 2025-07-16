from fastapi import FastAPI, Response

from src.routes.router import products_router



app = FastAPI()
app.include_router(products_router)


@app.get('/')
async def home():
  return Response(
    'Everything running!'
  )