identidade = input("Insire o seu número do BI? ")
resultado = identidade.strip()

#criando a base de dados das alunas
base_de_dados = {
    "004843261LA040": {
        "nome": "Alcina Eurico",
        "curso": ["Curso de Python","Desenvolvimento Web"],
        "computador": "Mediateca"
    },
    "004843261LA041": {
        "nome": "Deura Fernandes",
        "curso": ["Curso de Python","Desenvolvimento Web"],
        "computador": "Mediateca"
    },
    "004843261LA042": {
        "nome": "Deisy Costa",
        "curso": ["Curso de Python","Desenvolvimento Web"],
        "computador": "Pessoal"
    },
    "004843261LA043": {
        "nome": "Domingas Queta",
        "curso": ["Curso de Python","Desenvolvimento Web"],
        "computador": "Mediateca"
    },
    "004843261LA044": {
        "nome": "Elisa Mavinga",
        "curso": ["Curso de Python","Desenvolvimento Web"],
        "computador": "Mediateca"
    },
    "004843261LA045": {
        "nome": "Fernanda Zacarias",
        "curso": ["Curso de Python","Desenvolvimento Web"],
        "computador": "Mediateca"
    },
    "004843261LA046": {
        "nome": "Geunila Gomes",
        "curso": ["Curso de Python","Desenvolvimento Web"],
        "computador": "Mediateca"
    },

    "004843261LA047": {
        "nome": "Lauriane Vunge",
        "curso": ["Curso de Python","Desenvolvimento Web"],
        "computador": "Mediateca"
    },
    "004843261LA048": {
        "nome": "Isabel Pascoal",
        "curso": ["Curso de Python","Desenvolvimento Web"],
        "computador": "Mediateca"
    },
    "004843261LA049": {
        "nome": "Joice Calunga",
        "curso": ["Curso de Python","Desenvolvimento Web"],
        "computador": "Mediateca"
    },
    "004843261LA050":{
        "nome": "Liria Tomas",
        "curso": ["Curso de Python","Desenvolvimento Web"],
        "computador": "Mediateca"
        }
}

#retornar os dados inseridos pelo usuario
aluna = base_de_dados.get(resultado)

if aluna:
    print("Aluna foi encontrada com sucesso!")
    hora_de_entrada = input("Hora de Entrada")
    print(hora_de_entrada) 
else:
    print("O BI inserido não corresponde a nenhuma Aluna")

    


