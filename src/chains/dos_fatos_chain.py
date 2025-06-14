from models.dos_fatos_model import DosFatosModel
from langchain_core.prompts import ChatPromptTemplate
from chains.dos_fatos.prompt_data_cleaning import PromptDataCleaning





data_cleaning = DosFatosModel().model["data_cleaning"]
transcricao = "Oi, Dra. a loja online 'VendeTudo' não me entregou o celular que comprei. Fiz a compra no site dia 01 de março de 2025, paguei R$ 2.500,00 no PIX. O prazo era 10 dias, ou seja, dia 11 de março. Não chegou. Mandei email dia 12 e dia 15 de março, e eles nem responderam. O número do pedido é 12345."

# 2. Crie uma instância da sua classe
prompt_builder = PromptDataCleaning(user_input=transcricao)

# 3. Obtenha o prompt já formatado e pronto para usar com um LLM
#    Este é o objeto que você vai passar para a sua 'chain' ou modelo
prompt_final = prompt_builder.format_prompt()

# Para visualizar o que foi criado:
print(prompt_final)

if data_cleaning:
    # Só executa o invoke se a criação do modelo deu certo
    resposta = data_cleaning.invoke(prompt_final)
    print(resposta)
else:
    print("\nFalha ao criar o modelo. Encerrando o script.")