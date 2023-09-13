from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestData(BaseModel):
    data: dict


# @app.post("/test")

def test(request_data: RequestData):
    # Получаем данные из запроса
    data = request_data
    print('Получили data', data)

    return {"message": "Данные обработаны и успешно отправлены"}

