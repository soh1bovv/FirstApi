from fastapi import FastAPI, HTTPException

app = FastAPI()

news = [
    {'id': 1, 'title': 'post 1', 'body': 'text1'},
    {'id': 2, 'title': 'post 2', 'body': 'text2'},
    {'id': 3, 'title': 'post 3', 'body': 'text3'}

]
@app.get('/items')
async def items() -> list:
    return news

@app.get("/items/{id}")
async def get_item (id: int) -> dict:
    for new in news:
        if new['id'] == id:
            return new
    raise HTTPException(status_code=404, detail='News not found')


