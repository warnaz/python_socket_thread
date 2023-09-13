import click
import creds
import concurrent.futures
from get_client import get_spot_client

def send_order():
    # Размещение ордера
    click.secho("Отправка Заявки", fg="red")

    client = get_spot_client()

    r = client.depth(symbol='BTCBUSD', limit=1)
    best_buy = r.get('bids')[-1][0]

    r = client.new_order(
        symbol='BTCBUSD',
        quantity=0.001,
        side='BUY',
        type="LIMIT",
        price=best_buy,
        timeInForce="GTC"
    )

    print(r)


# Create a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit the send_order function to the executor multiple times
    # to run it concurrently
    futures = [executor.submit(send_order) for _ in range(1)]

    # Wait for all futures to complete
    concurrent.futures.wait(futures)
