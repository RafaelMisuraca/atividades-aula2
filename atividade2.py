frutas = {'maçã', 'uva', 'banana', 'laranja', 'morango'}

fruta_a_verificar = {"banana"}

resultado = frutas.intersection(fruta_a_verificar)
if resultado:
    print(f"A fruta {fruta_a_verificar} está presento no conjunto.")
else:
    print(f"A fruta {fruta_a_verificar} não faz parte do conjunto.")