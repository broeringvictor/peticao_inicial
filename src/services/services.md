#### 🗂️ **`services/`**: A Lógica de Negócio

Este diretório atua como uma ponte entre a sua aplicação (ex: uma API) e as cadeias LangChain. Ele orquestra as chamadas e aplica a lógica de negócio necessária.

- **`rag_service.py`**: Pode conter uma classe ou função que implementa a lógica de RAG (Retrieval-Augmented Generation). Ela usaria a `qa_chain` de `app/chains/`, buscaria informações em um _vector store_ e processaria a entrada do usuário para retornar uma resposta.