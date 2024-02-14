from fastapi import FastAPI
import uvicorn 

# Init App
app = FastAPI()


# Routes
@app.get('/')
async def index():
    return {"text":"Hello API Builders"}




if __name__ == '__main__':
    uvicorn.run(app,host="0.0.0.0", port=8000)
 