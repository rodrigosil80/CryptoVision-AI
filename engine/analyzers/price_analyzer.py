class PriceAnalyzer:

    def analisar(self, moeda: dict):

        variacao = moeda["price_change_percentage_24h"]
       
        if variacao > 5:
         score = 15
         motivo = "Preço em forte alta nas últimas 24 horas."

        elif variacao > 2:
         score = 8
         motivo = "Preço em alta moderada nas últimas 24 horas."

        elif variacao >= -2:
         score = 0
         motivo = "Preço em movimento lateral nas últimas 24 horas."
         
        elif variacao >= -5:
         score = -8
         motivo = "Preço em queda moderada nas últimas 24 horas."
         
        else:
         score = -15
         motivo = "Preço em forte queda nas últimas 24 horas."
         
        return {
        "score": score,
        "motivo": motivo
}