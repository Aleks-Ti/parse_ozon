# https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=/searchSuggestions/?text=&url=/seller/proffi-1/products/
import tls_client
from pprint import pprint

url = 'https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=/seller/proffi-1/products/' # ?page=1

session = tls_client.Session(
    client_identifier="chrome112", random_tls_extension_order=True
)

response = session.get(url)
response.status_code
d = response.json()
pprint(d)
