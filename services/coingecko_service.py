import requests


class CoinGeckoService:

    BASE_URL = "https://api.coingecko.com/api/v3"
    
    
    def get_coins(self):

        url = (
        f"{self.BASE_URL}/coins/markets"
        "?vs_currency=brl"
        "&ids=bitcoin,ethereum,solana"
    )

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        return []

    def get_coin(self, coin_id: str):

        moedas = self.get_coins()

        for moeda in moedas:

         if moeda["id"] == coin_id:
              return moeda

        return None
    
