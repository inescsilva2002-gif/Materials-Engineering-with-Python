class Metal:
    def __init__(self, nome, limite, resistencia):
        self.nome = nome
        self.limite = limite
        self.resistencia = resistencia

metais = [
    Metal("Aço S355", 355, 630),
    Metal("Aluminio Puro", 35, 90),
    Metal("Cobre Recozido", 70, 220),
    Metal ("Titanio Ti6Al4V", 900,1000)
]
        
print("Bem vindo a minha calculadora de tensão. Ainda está em desenvolvimento por isso só estão disponiveis 4 materiais: Aço S355, Aluminio Puro, Cobre recozido e Titanio Ti6Al4V")
#Inputs
material= input ("Qual é o material?")
força = float (input ("Qual é a força em N: "))
area = float (input ("Qual é a área em m^2: "))

#Calculos de tensão
tensao = força / area

#condiçoes
encontrado = False

for metal in metais :
    if metal.nome.lower() == material.lower().strip():
     encontrado=True
     if tensao > metal.resistencia :
        print (f"{material} fraturou")
     elif tensao > metal.limite :
        print (f"{material} entrou na zona plástica. "
               f"A tensão atual é {tensao} MPa e a resistência máxima é {metal.resistencia} MPa.")
     else: 
        print (f"{material} permanece na zona elástica. "
               f"A tensão atual é {tensao} MPa e o limite elástico é {metal.limite} MPa.")
if  encontrado==False:
       print (f"{material} não existe")