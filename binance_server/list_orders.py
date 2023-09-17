import click
import pandas as pd
from get_client import get_spot_client
import _creds

# Просто текст, выводящийся в терминал в синем цвете
click.secho("Список ордеров", fg="blue")


api_key = _creds.api_key
secret_key = _creds.secret_key


client = get_spot_client(api_key, secret_key)


print(pd.DataFrame(client.account().get('balances')))

df = pd.DataFrame(
    client.get_orders(symbol="BTCUSDT"),
    columns=['orderId', 'type', 'side', 'price', 'status']
)

print(df)
