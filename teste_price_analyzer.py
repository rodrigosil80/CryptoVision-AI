from engine.analyzers.price_analyzer import PriceAnalyzer

print("Teste iniciado")

analyzer = PriceAnalyzer()

moeda_teste = {
   "price_change_percentage_24h": -7.0
}

resultado = analyzer.analisar(moeda_teste)

print(resultado)