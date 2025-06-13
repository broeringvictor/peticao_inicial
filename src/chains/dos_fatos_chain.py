from models.dos_fatos_model import DosFatosModel



# Tenta criar o modelo
data_cleaning = DosFatosModel().model["data_cleaning"]



if data_cleaning:
    # Só executa o invoke se a criação do modelo deu certo
    resposta = data_cleaning.invoke("Olá, qual a sua função?")
    print(resposta)
else:
    print("\nFalha ao criar o modelo. Encerrando o script.")