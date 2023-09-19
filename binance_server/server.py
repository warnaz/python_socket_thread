from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()


class RequestData(BaseModel):
    data: dict


def process_data_sync(data):
    # Обрабатываем данные
    from stream import main
    main(data)


async def process_data_async(data):
    await asyncio.to_thread(process_data_sync, data)


@app.post("/process_data")
async def process_data(request_data: RequestData):
    # Получаем данные из запроса
    data = request_data.data

    print('------- Подключение клиента -------', end='\n')

    # Запускаем обработку данных асинхронно
    await process_data_async(data)

    return {"message": "Данные обработаны и успешно отправлены"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
