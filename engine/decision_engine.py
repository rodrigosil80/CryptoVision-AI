class DecisionEngine:

    def __init__(self, market_service):
        self.market_service = market_service

    def analisar(self, coin_id: str):
        
        moeda = self.market_service.get_coin(coin_id)

        return {
            "nome": moeda["name"],
            "preco": moeda["current_price"],
            "variacao": moeda["price_change_percentage_24h"],
            "confianca": 50,
            "cenario": "Neutro",
            "motivos": [
                "Análise inicial baseada em regras simples."
            ],
            "riscos": [
                "Poucos indicadores disponíveis."
            ]
        }