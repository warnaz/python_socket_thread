from time import sleep
import creds
import click
from binance.websocket.spot.websocket_client import SpotWebsocketClient
import httpx
from get_client import get_spot_client
from client_server import test

def _user_data(r):
    """
    Подписка на user_data
    :param r:
    :return:
    """
    if 'e' in r:
        if r.get('e') == 'executionReport':
            
            # Логи в консоль
            id = r.get('c')
            sym = r.get('s')
            print(f"Изменились заявки {sym} / {id}")

            if r.get('X') == 'NEW':
                print("Размещение лимитки")
            elif r.get('X') == 'FILLED':
                click.secho(f"Заяка {id} исполнилась", fg='green')
        
        # Отправка данных на API методом post
        try:
            test(request_data=r)
            # response = httpx.post("http://test", json={"processed_data": r})
            # response.raise_for_status()
        except Exception as e:
            print(e)
    else:
        print("Подписка user_data")


def main(data):
    # ************ Запуск сокета ************
    click.secho("Поднимаю Stream", fg='magenta')

    client = SpotWebsocketClient(stream_url="wss://testnet.binance.vision")
    client.start()

    try:
        api_key = data.get('api_key')
        secret_key = data.get('sec_key')

        listen_key = get_spot_client(api_key, secret_key).new_listen_key().get("listenKey")
        client.user_data(listen_key=listen_key, id=1, callback=_user_data)

        # Обновление listen_key каждый час
        for i in range(1, 60*60*24):
            if listen_key and i % 59*60 == 0: get_spot_client(api_key, secret_key).renew_listen_key(listen_key)
            if i % 60 == 0:
                click.secho(f"Сокет ок, {int(i/60)} мин.", fg="yellow")
            sleep(1)

    except KeyboardInterrupt:
        ...
    finally:
        client.stop()
