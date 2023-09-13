import click
from get_client import get_spot_client

click.secho("Отправка Заявки", fg="red")

client = get_spot_client()

r = client.depth(symbol='BTCUSDT', limit=10)
best_buy = r.get('bids')[-1][0]
print('What', best_buy)

r = client.new_order(
    symbol='BTCUSDT',
    quantity=0.001,
    side='BUY',
    type="LIMIT",
    price=best_buy,
    timeInForce="GTC"
)

# r = client.cancel_open_orders(creds.symbol)
# print(r)
