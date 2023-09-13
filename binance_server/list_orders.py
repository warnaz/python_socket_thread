import click
import pandas as pd
from get_client import get_spot_client


# Просто текст, выводящийся в терминал в синем цвете
click.secho("Список ордеров", fg="blue")

client = get_spot_client()


print(pd.DataFrame(client.account().get('balances')))

df = pd.DataFrame(
    client.get_orders(symbol="BTCUSDT"),
    columns=['orderId', 'type', 'side', 'price', 'status']
)

print(df)
