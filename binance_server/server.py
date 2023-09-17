from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class RequestData(BaseModel):
    data: dict


@app.post("/process_data")
async def process_data(request_data: RequestData):
    # Получаем данные из запроса
    data = request_data.data
    print(data)

    # Обрабатываем данные
    from stream import main
    main(data)

    return {"message": "Данные обработаны и успешно отправлены"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
