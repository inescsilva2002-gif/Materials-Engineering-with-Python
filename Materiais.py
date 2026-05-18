class Metal:
    def __init__(self, nome, densidade, resistencia, preco):
        self.nome = nome
        self.densidade = densidade
        self.resistencia = resistencia
        self.preco = preco


metais = [
    Metal("Aço Carbono", 7.85, 400, 1),
    Metal("Alumínio", 2.70, 310, 2),
    Metal("Cobre", 8.96, 220, 3)
]

# Perguntas ao utilizador
densidade_max = float(input("Densidade máxima: "))
resistencia_min = float(input("Resistência mínima: "))
print("Preço encontra-se numa escala de 1 a 3")
preco_max = int(input("Preço máximo: "))

# Procurar metais compatíveis
print("\nMateriais encontrados:\n")

for metal in metais:
    if (
        metal.densidade <= densidade_max
        and metal.resistencia >= resistencia_min
        and metal.preco <= preco_max
    ):
        print(metal.nome) 