# No seu arquivo que usa a fábrica, como dos_fatos_chain.py

from core.llm_factory import LLMFactory

# Tenta criar o modelo
gemini = LLMFactory.create(
    "gemini-1.5-flash", 
    model_provider="google_genai", 
    temperature=0.7
)


if gemini:
    # Só executa o invoke se a criação do modelo deu certo
    resposta = gemini.invoke("Olá, qual a sua função?")
    print(resposta)
else:
    print("\nFalha ao criar o modelo. Encerrando o script.")