Este diretório é responsável por inicializar e configurar os modelos de linguagem (LLMs) e os modelos de embedding.

- **`llm.py`**: Aqui você centraliza a criação das instâncias dos seus LLMs (ex: `ChatOpenAI`, `GoogleGenerativeAI`) e dos modelos de embedding (ex: `OpenAIEmbeddings`). Isso permite que você troque de modelo facilmente em um único lugar, sem precisar alterar o resto do código.